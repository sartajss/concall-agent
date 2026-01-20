# Concall Analysis Agent (Gemma + Ollama)

This project analyzes company conference call transcripts (PDF) and produces:

- High-level summary
- Management tone (Bullish / Neutral / Bearish)
- Triggers for:
  - Next 0–3 months
  - Next 3–6 months
  - Beyond 6 months

## Install dependencies
pip install -r requirements.txt

## Run
python run_concall_agent.py data/sample_concall.pdf