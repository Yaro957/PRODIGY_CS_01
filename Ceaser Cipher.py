
def encrypt(text, shift):
    dictsmall = {
        'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11,
        'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22,
        'x': 23, 'y': 24, 'z': 25
    }
    dictup = {
        'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11,
        'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22,
        'X': 23, 'Y': 24, 'Z': 25
    }
    dictsmall_inv = {v: k for k, v in dictsmall.items()}
    dictup_inv = {v: k for k, v in dictup.items()}

    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                result += dictsmall_inv[(dictsmall[char] + shift) % 26]
            elif char.isupper():
                result += dictup_inv[(dictup[char] + shift) % 26]
        else:
            result += char
    return result

choice = input("Type 'encrypt' for encryption and 'decrypt' for decryption\n")

if choice == "encrypt":
    text = input("Enter the text\n")
    key = int(input("Enter the shift key\n"))
    encrypted_text = encrypt(text, key)
    print(f"Encrypted text is: {encrypted_text}")

elif choice == "decrypt":
    text = input("Enter the text\n")
    key = int(input("Enter the shift key\n"))
    decrypted_text = encrypt(text, -key)
    print(f"Decrypted text is: {decrypted_text}")