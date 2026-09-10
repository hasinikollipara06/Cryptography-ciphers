def valid_message(text):
    for ch in text:
        if not (ch.isalpha() or ch in " \n"):
            return False
    return True


def clean_text(text):
    text = text.upper()
    return text.replace(" ", "").replace("\n", "")


def generate_matrix(key):
    matrix = []
    used = set()

    key = key.upper().replace("J", "I")

    for ch in key:
        if ch not in used and 'A' <= ch <= 'Z':
            matrix.append(ch)
            used.add(ch)

    for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch not in used:
            matrix.append(ch)
            used.add(ch)

    return [matrix[i:i + 5] for i in range(0, 25, 5)]


def prepare_pairs(text):
    result = ""
    i = 0

    while i < len(text):
        first = 'I' if text[i] == 'J' else text[i]

        if i + 1 >= len(text):
            result += first + "X"
            break

        second = 'I' if text[i + 1] == 'J' else text[i + 1]

        if first == second:
            result += first + "X"
            i += 1
        else:
            result += first + second
            i += 2

    return result


def find_position(matrix, ch):
    if ch == 'J':
        ch = 'I'

    for row in range(5):
        for col in range(5):
            if matrix[row][col] == ch:
                return row, col


def encrypt(text, matrix):
    output = ""

    for i in range(0, len(text), 2):
        r1, c1 = find_position(matrix, text[i])
        r2, c2 = find_position(matrix, text[i + 1])

        if r1 == r2:
            output += matrix[r1][(c1 + 1) % 5]
            output += matrix[r2][(c2 + 1) % 5]

        elif c1 == c2:
            output += matrix[(r1 + 1) % 5][c1]
            output += matrix[(r2 + 1) % 5][c2]

        else:
            output += matrix[r1][c2]
            output += matrix[r2][c1]

    return output


def decrypt(text, matrix):
    output = ""

    for i in range(0, len(text), 2):
        r1, c1 = find_position(matrix, text[i])
        r2, c2 = find_position(matrix, text[i + 1])

        if r1 == r2:
            output += matrix[r1][(c1 - 1) % 5]
            output += matrix[r2][(c2 - 1) % 5]

        elif c1 == c2:
            output += matrix[(r1 - 1) % 5][c1]
            output += matrix[(r2 - 1) % 5][c2]

        else:
            output += matrix[r1][c2]
            output += matrix[r2][c1]

    return output


message = input("Enter the text: ")

if not valid_message(message):
    print("Invalid input! Digits and special symbols are not permitted.")

else:
    message = clean_text(message)

    keyword = input("Enter the key: ")

    if not valid_message(keyword):
        print("Invalid key! Use alphabetic characters only.")

    else:
        keyword = clean_text(keyword)
        playfair_matrix = generate_matrix(keyword)

        print("\nGenerated Playfair Matrix:")
        for row in playfair_matrix:
            print(" ".join(row))

        print("\n1. Encrypt")
        print("2. Decrypt")

        choice = int(input("Select an operation: "))

        if choice == 1:
            prepared = prepare_pairs(message)

            print("\nPrepared text:", prepared)
            print("J is replaced with I and repeated letters are separated by X.")

            cipher_text = encrypt(prepared, playfair_matrix)
            print("Encrypted text:", cipher_text)

        elif choice == 2:
            cipher_text = message.replace("J", "I")

            print("\nCipher text:", cipher_text)

            plain_text = decrypt(cipher_text, playfair_matrix)
            print("Decrypted text:", plain_text)

        else:
            print("Invalid choice!")