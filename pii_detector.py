import re

def detect_pii(text):

    phone_pattern = r'\b\d{11}\b'
    email_pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'

    phone_match = re.search(phone_pattern, text)
    email_match = re.search(email_pattern, text)

    if phone_match:
        print("📱 Phone number detected")
        text = re.sub(phone_pattern, "[PHONE_MASKED]", text)

    if email_match:
        print("📧 Email detected")
        text = re.sub(email_pattern, "[EMAIL_MASKED]", text)

    return text

