"""Laugh-off writer: one fixed office joke about headphones and managers."""

import os, string, sys

TEXT = "I put my headphones on to signal I'm busy. My manager now schedules meetings by tapping my shoulder twice, like I'm a vending machine."
LIMIT = 200
ENDERS = ".!?"

def fail(msg):
    sys.stderr.write("invalid: " + msg + "\n")
    raise SystemExit(1)

def validate(text):
    lowered = text.casefold()
    rules = [
        ("manager" not in lowered, "must mention the manager"),
        (not text.strip(), "blank entry"),
        (len(text) > LIMIT, "over 200 characters"),
        (any(ord(c) < 32 or ord(c) == 127 for c in text), "control character found"),
        (text != text.strip() or "  " in text or "\n" in text, "ragged edges, double space, or newline"),
        (bool(text) and text[-1] not in ENDERS, "must end with . ! or ?"),
        (all(c in string.punctuation for c in text), "punctuation only"),
        (text.isdigit(), "digits only"),
        (not any(c.isalpha() for c in text), "no letters"),
        ("!" in text, "shouts with an exclamation mark"),
        ("---" in text, "triple hyphen"),
    ]
    for bad, msg in rules:
        if bad:
            fail(msg)

def write_out():
    validate(TEXT)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(TEXT + "\n")

if __name__ == "__main__":
    write_out()
