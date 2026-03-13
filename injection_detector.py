# injection_detector.py

def detect_prompt_injection(text):
    """
    Detects possible prompt injection or jailbreak attempts
    in the user's input text.
    Returns True if suspicious content is found.
    """

    # Convert text to lowercase for easier comparison
    text = text.lower()

    # List of common prompt injection / jailbreak phrases
    suspicious_phrases = [
        "ignore previous instructions",
        "ignore all instructions",
        "reveal system prompt",
        "show system prompt",
        "what is your system prompt",
        "act as an unrestricted ai",
        "bypass safety",
        "jailbreak",
        "do anything now",
        "pretend you are not restricted",
        "forget previous rules"
    ]

    # Check if any suspicious phrase appears in the text
    for phrase in suspicious_phrases:
        if phrase in text:
            return True

    # If nothing suspicious found
    return False