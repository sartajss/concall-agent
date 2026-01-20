from typing import List
from .ollama_client import OllamaLLM
from .pdf_utils import load_pdf_text, chunk_text
from .prompts import ANALYSIS_PROMPT_TEMPLATE

class ConcallAnalysisAgent:
    def __init__(self, model: str = "gemma:2b"):
        self.llm = OllamaLLM(model=model)

    def _analyze_chunk(self, chunk: str) -> str:
        prompt = ANALYSIS_PROMPT_TEMPLATE.format(chunk=chunk)
        return self.llm.generate(prompt)

    def _merge_analyses(self, analyses: List[str]) -> str:
        all_analyses = "\\n\\n--- CHUNK ANALYSIS SEPARATOR ---\\n\\n".join(analyses)

        merge_prompt = f"""
You are an equity research analyst.

You are given multiple structured analyses of different chunks of the SAME company conference call transcript.

Your job:
1. Merge them into ONE coherent report.
2. Resolve inconsistencies.
3. Keep the same Markdown structure:

# High-level summary
# Management tone
# Triggers: next 0–3 months
# Triggers: next 3–6 months
# Triggers: beyond 6 months

Here are the chunk-level analyses:

\"\"\"{all_analyses}\"\"\"
"""
        return self.llm.generate(merge_prompt)

    def analyze_concall_pdf(self, pdf_path: str) -> str:
        full_text = load_pdf_text(pdf_path)
        chunks = chunk_text(full_text, max_chars=6000)

        if not chunks:
            return "# Error\\n\\nNo text could be extracted from the PDF."

        chunk_analyses = []
        for i, chunk in enumerate(chunks, start=1):
            print(f"[ConcallAnalysisAgent] Analyzing chunk {i}/{len(chunks)}...")
            analysis = self._analyze_chunk(chunk)
            chunk_analyses.append(analysis)

        if len(chunk_analyses) == 1:
            return chunk_analyses[0]

        print("[ConcallAnalysisAgent] Merging chunk analyses into final report...")
        return self._merge_analyses(chunk_analyses)
