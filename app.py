from modules.input_handler import get_user_input
from modules.injection_detector import detect_injection
from modules.presidio_analyzer import analyze_pii
from modules.policy_engine import decide_policy
from modules.output_handler import display_result

def main():

    user_input = get_user_input()

    injection_score = detect_injection(user_input)

    pii_entities, masked_text = analyze_pii(user_input)

    decision = decide_policy(injection_score, pii_entities)

    display_result(user_input, masked_text, injection_score, pii_entities, decision)


if __name__ == "__main__":
    main()