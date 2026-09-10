def remove_spaces(text):
    return text.replace(" ", "").replace("\n", "")


def encrypt(text, rails):
    result = ""

    for current_rail in range(rails):
        row = 0
        direction = 1

        for ch in text:
            if row == current_rail:
                result += ch

            if row == rails - 1:
                direction = -1
            elif row == 0:
                direction = 1

            row += direction

    return result


def decrypt(cipher, rails):
    length = len(cipher)

    # Find the rail pattern for each character
    pattern = []
    row = 0
    direction = 1

    for i in range(length):
        pattern.append(row)

        if row == rails - 1:
            direction = -1
        elif row == 0:
            direction = 1

        row += direction

    # Count characters present in every rail
    rail_count = [0] * rails

    for r in pattern:
        rail_count[r] += 1

    # Store the starting position of each rail
    rail_start = [0] * rails
    total = 0

    for r in range(rails):
        rail_start[r] = total
        total += rail_count[r]

    # Reconstruct the original message
    current_pos = rail_start[:]
    plain = [""] * length

    for i in range(length):
        r = pattern[i]
        plain[i] = cipher[current_pos[r]]
        current_pos[r] += 1

    return "".join(plain)


text = input("Enter the message: ")
text = remove_spaces(text)

print("Text after space removal:", text)

rails = int(input("Enter the number of rails: "))

if rails < 2 or rails > len(text):
    print("Invalid rail count!")
else:
    print("\nSelect the operation:")
    print("1. Encryption")
    print("2. Decryption")

    choice = int(input("Enter option number: "))

    if choice == 1:
        encrypted_text = encrypt(text, rails)
        print("Encrypted text:", encrypted_text)

    elif choice == 2:
        decrypted_text = decrypt(text, rails)
        print("Decrypted text:", decrypted_text)

    else:
        print("Invalid option selected.")