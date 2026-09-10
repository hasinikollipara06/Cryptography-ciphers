def check_input(text):
    for ch in text:
        if not (ch.isalpha() or ch in " \n"):
            return False
    return True


def encrypt(text, key):
    result = ""
    key_pos = 0
    key_len = len(key)

    for ch in text:
        if 'A' <= ch <= 'Z':
            shift = ord(key[key_pos % key_len]) - ord('A')
            result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
            key_pos += 1

        elif 'a' <= ch <= 'z':
            shift = ord(key[key_pos % key_len]) - ord('a')
            result += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
            key_pos += 1

        else:
            result += ch

    return result


def decrypt(text, key):
    result = ""
    key_pos = 0
    key_len = len(key)

    for ch in text:
        if 'A' <= ch <= 'Z':
            shift = ord(key[key_pos % key_len]) - ord('A')
            result += chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))
            key_pos += 1

        elif 'a' <= ch <= 'z':
            shift = ord(key[key_pos % key_len]) - ord('a')
            result += chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))
            key_pos += 1

        else:
            result += ch

    return result


plain_text = input("Enter the message: ")

if not check_input(plain_text):
    print("Invalid message! Digits and special characters are not accepted.")
else:
    key = input("Enter the key: ").upper()

    print("\nChoose an operation:")
    print("1. Encrypt")
    print("2. Decrypt")

    option = int(input("Enter your option: "))

    if option == 1:
        cipher_text = encrypt(plain_text, key)
        print("Result after encryption:", cipher_text)

    elif option == 2:
        original_text = decrypt(plain_text, key)
        print("Result after decryption:", original_text)

    else:
        print("Invalid option selected.")