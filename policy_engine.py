# policy_engine.py

def apply_policy(text):
    """
    Simple policy engine that decides whether to
    ALLOW, MASK, or BLOCK the request.
    """

    # Block if sensitive system prompts are requested
    blocked_keywords = [
        "system prompt",
        "ignore previous instructions",
        "reveal secrets",
        "show hidden instructions"
    ]

    for word in blocked_keywords:
        if word.lower() in text.lower():
            return "BLOCK"

    # If nothing suspicious
    return "ALLOW"