def valid_text(text):
    for ch in text:
        if not (ch.isalpha() or ch.isdigit() or ch in " \n"):
            return False
    return True


def encrypt(text, shift):
    result = ""
    shift = shift % 26

    for ch in text:
        if 'A' <= ch <= 'Z':
            result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))

        elif 'a' <= ch <= 'z':
            result += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))

        elif '0' <= ch <= '9':
            digit_shift = shift % 10
            result += chr((ord(ch) - ord('0') + digit_shift) % 10 + ord('0'))

        else:
            result += ch

    return result


def decrypt(text, shift):
    result = ""
    shift = shift % 26

    for ch in text:
        if 'A' <= ch <= 'Z':
            result += chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))

        elif 'a' <= ch <= 'z':
            result += chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))

        elif '0' <= ch <= '9':
            digit_shift = shift % 10
            result += chr((ord(ch) - ord('0') - digit_shift) % 10 + ord('0'))

        else:
            result += ch

    return result


text = input("Enter the text: ")

if not valid_text(text):
    print("Special characters are not supported!")
else:
    key = int(input("Enter the shift value: "))

    print("\nSelect the required operation:")
    print("1. Encryption")
    print("2. Decryption")

    choice = int(input("Enter option: "))

    if choice == 1:
        output = encrypt(text, key)
        print("Encrypted text:", output)

    elif choice == 2:
        output = decrypt(text, key)
        print("Decrypted text:", output)

    else:
        print("Invalid option!")