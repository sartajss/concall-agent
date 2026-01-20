import sys
from pathlib import Path
from agent.concall_analysis_agent import ConcallAnalysisAgent

def main():
    if len(sys.argv) < 2:
        print("Usage: python run_concall_agent.py amd_concall.pdf")
        sys.exit(1)

    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        print(f"Error: file not found: {pdf_path}")
        sys.exit(1)

    agent = ConcallAnalysisAgent(model="gemma:2b")
    report = agent.analyze_concall_pdf(str(pdf_path))

    print("\\n\\n===== FINAL ANALYSIS =====\\n")
    print(report)

if __name__ == "__main__":
    main()
