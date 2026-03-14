import re

def detect_pii(text):

    # Patterns
    phone_pattern = r'\b\d{11}\b'
    email_pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
    api_pattern = r'sk-[A-Za-z0-9]{10,40}'

    risk_score = 0

    # Phone detection
    if re.search(phone_pattern, text):
        print("📱 Phone number detected")
        text = re.sub(phone_pattern, "[PHONE_MASKED]", text)
        risk_score += 0.3

    # Email detection
    if re.search(email_pattern, text):
        print("📧 Email detected")
        text = re.sub(email_pattern, "[EMAIL_MASKED]", text)
        risk_score += 0.3

    # Custom Recognizer (API Key)
    if re.search(api_pattern, text):
        print("🔑 API Key detected")
        text = re.sub(api_pattern, "[API_KEY_MASKED]", text)
        risk_score += 0.5

    # Context-Aware Detection
    if "password" in text.lower() or "secret" in text.lower():
        print("⚠ Sensitive context detected")
        risk_score += 0.3

    # Confidence Calibration
    threshold = 0.3

    if risk_score >= threshold:
        return True, text
    else:
        return False, text