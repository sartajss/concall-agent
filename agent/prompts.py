ANALYSIS_PROMPT_TEMPLATE = """
You are analyzing a single company's earnings / conference call transcript.

IMPORTANT RULES:
- Identify the ONE primary company whose earnings call this is.
- Ignore all other companies mentioned (competitors, partners, customers, suppliers, etc.).
- Ignore analyst firm names (e.g., BofA, Morgan Stanley).
- Do NOT treat executive names (e.g., Lisa Su, Satya Nadella) as companies.
- If another company is mentioned, treat it ONLY as context, not as a separate entity.

Your tasks:

1. Extract the primary company details:
   - Company name
   - Ticker (if mentioned)
   - Sector / industry (infer if needed)
   - Quarter or period (if mentioned)

2. Create a concise, high‑quality summary of the call focused ONLY on the primary company.

3. Infer management tone (Bullish / Neutral / Bearish) based ONLY on the primary company’s commentary.

4. Extract forward‑looking triggers for the primary company:
   - Next 0–3 months
   - Next 3–6 months
   - Beyond 6 months

Return the answer in this structure:

# Company details
- Name: <primary company>
- Ticker: <ticker or "not mentioned">
- Sector: <sector or inferred>
- Period: <quarter/year or "not mentioned">

# High‑level summary
- ...

# Management tone
- Overall tone: <Bullish / Neutral / Bearish>
- Rationale:
  - ...

# Triggers: next 0–3 months
- ...

# Triggers: next 3–6 months
- ...

# Triggers: beyond 6 months
- ...

Use ONLY information from the transcript chunk below.
If something is not mentioned, write "not mentioned".

Transcript chunk:
\"\"\"{chunk}\"\"\"
"""
