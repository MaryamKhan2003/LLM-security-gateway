from pii_detector import detect_pii
from input_handler import get_user_input
from injection_detector import detect_prompt_injection
from policy_engine import apply_policy
import requests


def query_llm(prompt):

    url = "http://localhost:11434/api/generate"

    data = {
        "model": "tinyllama",   # or tinyllama
        "temperature": 0.8,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=data)
    result = response.json()

    return result.get("response", "No response from model")


def main():

    text = get_user_input()

    attack = detect_prompt_injection(text)

    if attack:
        print("⚠ Prompt Injection Detected")
        print("❌ Request blocked by security policy")
        return

    sanitized_text = detect_pii(text)

    print("\nInput Sent to LLM:")
    print(sanitized_text)

    response = query_llm(sanitized_text)

    print("\nLLM Response:")
    print(response)


if __name__ == "__main__":
    main()