def remove_spaces(text):
    return text.replace(" ", "").replace("\n", "")


def get_order(key):
    order = [0] * len(key)

    for i in range(len(key)):
        for j in range(len(key)):
            if key[j] < key[i]:
                order[i] += 1
            elif key[j] == key[i] and j < i:
                order[i] += 1

    return order


def encrypt(text, key):
    columns = len(key)
    rows = (len(text) + columns - 1) // columns

    matrix = []
    position = 0

    # Fill the matrix row by row
    for i in range(rows):
        row = []

        for j in range(columns):
            if position < len(text):
                row.append(text[position])
                position += 1
            else:
                row.append('X')

        matrix.append(row)

    order = get_order(key)
    cipher = ""

    # Read columns according to their alphabetical order
    for number in range(columns):
        for col in range(columns):
            if order[col] == number:
                for row in range(rows):
                    cipher += matrix[row][col]

    return cipher


def decrypt(cipher, key):
    columns = len(key)
    rows = (len(cipher) + columns - 1) // columns

    matrix = [[''] * columns for _ in range(rows)]
    order = get_order(key)

    position = 0

    # Put ciphertext back into columns
    for number in range(columns):
        for col in range(columns):
            if order[col] == number:
                for row in range(rows):
                    matrix[row][col] = cipher[position]
                    position += 1

    # Read the matrix row by row
    plain = ""

    for row in range(rows):
        for col in range(columns):
            plain += matrix[row][col]

    return plain


text = input("Enter the message: ")
text = remove_spaces(text)

print("Message after removing spaces:", text)

key1 = input("Enter the first key: ")
key1 = remove_spaces(key1)

key2 = input("Enter the second key: ")
key2 = remove_spaces(key2)

print("\nSelect the required operation:")
print("1. Encryption")
print("2. Decryption")

choice = int(input("Enter your choice: "))

if choice == 1:
    first_stage = encrypt(text, key1)
    final_cipher = encrypt(first_stage, key2)

    print("\nAfter first transposition:", first_stage)
    print("Final encrypted message:", final_cipher)

elif choice == 2:
    first_stage = decrypt(text, key2)
    original_text = decrypt(first_stage, key1)

    print("\nAfter reversing the second transposition:", first_stage)
    print("Recovered message:", original_text)

else:
    print("Invalid choice!")