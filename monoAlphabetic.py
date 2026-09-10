def make_upper(text):
    return text.upper()


def remove_spaces(text):
    return text.replace(" ", "").replace("\n", "")


def check_valid(text):
    for ch in text:
        if not (ch.isalpha() or ch in " \n"):
            return False
    return True


def encrypt(text, key):
    result = ""

    for ch in text:
        result += key[ord(ch) - ord('A')]

    return result


def decrypt(text, key):
    result = ""

    for ch in text:
        for i in range(26):
            if key[i] == ch:
                result += chr(i + ord('A'))
                break

    return result


# Substitution cipher key
key = "QWERTYUIOPASDFGHJKLZXCVBNM"

message = input("Enter the message: ")

if not check_valid(message):
    print("Invalid input! Digits and special characters are not permitted.")
else:
    message = make_upper(message)
    message = remove_spaces(message)

    print("Message without spaces:", message)
    print("Cipher key:", key)

    print("\nChoose an operation:")
    print("1. Encrypt")
    print("2. Decrypt")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        encrypted = encrypt(message, key)
        print("Encrypted text:", encrypted)

    elif choice == 2:
        decrypted = decrypt(message, key)
        print("Decrypted text:", decrypted)

    else:
        print("Invalid choice entered.")