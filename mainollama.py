import time
import ollama

from input_handler import get_user_input
from injection_detector import detect_prompt_injection
from pii_detector import detect_pii
from policy_engine import policy_decision


def main():

    text = get_user_input()

    start_time = time.time()

    injection = detect_prompt_injection(text)
    pii_detected, masked_text = detect_pii(text)

    decision = policy_decision(injection, pii_detected)

    gateway_time = time.time()

    if decision == "BLOCK":
        print("Request Blocked")
        return

    if decision == "MASK":
        text = masked_text

    # Query TinyLlama
    response = ollama.chat(
        model="tinyllama",
        messages=[{"role": "user", "content": text}]
    )

    end_time = time.time()

    gateway_latency = (gateway_time - start_time) * 1000
    total_latency = (end_time - start_time) * 1000

    print("\n------ Evaluation Output ------")
    print("Input:", text)
    print("Gateway Latency:", round(gateway_latency,2), "ms")
    print("Total Latency (Gateway + LLM):", round(total_latency,2), "ms")
    print("LLM Response:", response['message']['content'])


if __name__ == "__main__":
    main()