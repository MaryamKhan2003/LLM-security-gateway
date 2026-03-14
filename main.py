import time
import ollama

from input_handler import get_user_input
from injection_detector import detect_prompt_injection
from pii_detector import detect_pii
from policy_engine import policy_decision


def query_llm(prompt):
    response = ollama.chat(
        model="tinyllama",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['message']['content']


def main():

    text = get_user_input()

    start_time = time.time()

    injection_result = detect_prompt_injection(text)

    pii_result, masked_text = detect_pii(text)

    decision = policy_decision(injection_result, pii_result)

    gateway_time = time.time()

    if decision == "BLOCK":
        print("Request Blocked")
        return

    if decision == "MASK":
        text = masked_text

    # LLM call
    llm_response = query_llm(text)

    end_time = time.time()

    gateway_latency = (gateway_time - start_time) * 1000
    total_latency = (end_time - start_time) * 1000

    print("\n----- Evaluation Output -----")
    print("Input:", text)
    print("Gateway Latency:", gateway_latency, "ms")
    print("Total Latency (Gateway + LLM):", total_latency, "ms")
    print("LLM Response:", llm_response)


if __name__ == "__main__":
    main()