import string

def caesar(text, shift):
    def shift_char(ch, shift):
        if ch in string.ascii_lowercase:
            alphabet = list(string.ascii_lowercase)
        elif ch in string.ascii_uppercase:
            alphabet = list(string.ascii_uppercase)
        else:
            return ch
        shift %= len(alphabet)  # wrap the shift amount around the length of the alphabet
        return alphabet[(alphabet.index(ch) + shift) % len(alphabet)]

    encrypted_text = ""
    for ch in text:
        encrypted_text += shift_char(ch, shift)
    return encrypted_text

plain_text = input("What to encrypt?: ")
shift_amount = int(input("How many times to shift: "))
encrypted_text = caesar(plain_text, shift_amount)
print(encrypted_text)

