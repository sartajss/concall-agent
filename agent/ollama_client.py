import requests

class OllamaLLM:
    def __init__(self, model="gemma:2b", host="http://localhost:11434"):
        self.model = model
        self.host = host.rstrip("/")

    def generate(self, prompt: str) -> str:
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
        }
        response = requests.post(f"{self.host}/api/generate", json=payload)
        response.raise_for_status()
        return response.json().get("response", "").strip()
