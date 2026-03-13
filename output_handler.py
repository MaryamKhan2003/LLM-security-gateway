def display_result(original, masked, score, pii, decision):

    print("\n------ SECURITY GATEWAY RESULT ------")

    print("Original Input:")
    print(original)

    print("\nInjection Score:")
    print(score)

    print("\nDetected PII:")
    print(pii)

    print("\nDecision:")
    print(decision)

    if decision == "MASK":
        print("\nMasked Output:")
        print(masked)