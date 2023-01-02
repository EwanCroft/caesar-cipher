import string

def caesar(text, shift):
    shift %= 26  # wrap the shift amount around the length of the alphabet
    lower = list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)
    encrypted_text = ""
    for ch in text:
        if ch in lower:
            encrypted_text += lower[(lower.index(ch) + shift) % len(lower)]
        elif ch in upper:
            encrypted_text += upper[(upper.index(ch) + shift) % len(upper)]
        else:
            encrypted_text += ch
    return encrypted_text

plain_text = input("What to encrypt?: ")
shift_amount = int(input("How many times to shift: "))
encrypted_text = caesar(plain_text, shift_amount)
print(encrypted_text)
