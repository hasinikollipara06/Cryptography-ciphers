def validate_message(text):
    for ch in text:
        if not (ch.isalpha() or ch in " \n"):
            return False
    return True


def prepare_text(text):
    text = text.upper()
    text = text.replace(" ", "").replace("\n", "")

    if len(text) % 2 != 0:
        text += "X"

    return text


def encrypt(text, key):
    result = ""

    for i in range(0, len(text), 2):
        x1 = ord(text[i]) - ord('A')
        x2 = ord(text[i + 1]) - ord('A')

        y1 = (key[0][0] * x1 + key[0][1] * x2) % 26
        y2 = (key[1][0] * x1 + key[1][1] * x2) % 26

        result += chr(y1 + ord('A'))
        result += chr(y2 + ord('A'))

    return result


def find_inverse_determinant(det):
    for value in range(1, 26):
        if (det * value) % 26 == 1:
            return value
    return None


def decrypt(text, key):
    det = (key[0][0] * key[1][1] -
           key[0][1] * key[1][0]) % 26

    inverse_det = find_inverse_determinant(det)

    if inverse_det is None:
        return None

    inverse_key = [
        [(key[1][1] * inverse_det) % 26,
         (-key[0][1] * inverse_det) % 26],

        [(-key[1][0] * inverse_det) % 26,
         (key[0][0] * inverse_det) % 26]
    ]

    result = ""

    for i in range(0, len(text), 2):
        x1 = ord(text[i]) - ord('A')
        x2 = ord(text[i + 1]) - ord('A')

        y1 = (inverse_key[0][0] * x1 +
              inverse_key[0][1] * x2) % 26

        y2 = (inverse_key[1][0] * x1 +
              inverse_key[1][1] * x2) % 26

        result += chr(y1 + ord('A'))
        result += chr(y2 + ord('A'))

    return result


message = input("Enter the message: ")

if not validate_message(message):
    print("Invalid input! Numbers and special characters are not allowed.")

else:
    message = prepare_text(message)

    print("Prepared text:", message)

    print("Enter the 2 x 2 key matrix:")
    key_matrix = []

    for i in range(2):
        row = list(map(int, input().split()))
        key_matrix.append(row)

    print("\nSelect operation:")
    print("1. Encryption")
    print("2. Decryption")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        cipher = encrypt(message, key_matrix)
        print("Encrypted text:", cipher)

    elif choice == 2:
        plain = decrypt(message, key_matrix)

        if plain is None:
            print("The given key matrix cannot be inverted modulo 26.")
        else:
            print("Decrypted text:", plain)

    else:
        print("Invalid choice!")