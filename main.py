import random


def generate_table(alphabet):
    letter_deep = [14, 7, 2, 5, 2, 1, 3, 5, 1, 1, 2, 6, 5, 1, 1, 4, 3, 3, 7, 9, 3, 5, 4, 5, 3, 1, 1, 1, 1, 1, 1, 2, 1, 2]
    letter_amount = 34
    table = []
    for i in range(letter_amount):
        table.append([0] * letter_deep[i])
    for i in range(100, 100 + sum(letter_deep)):
        while True:
            random_i = random.randint(0, letter_amount - 1)
            if 0 in table[random_i]:
                random_j = table[random_i].index(0)
                table[random_i][random_j] = i
                break
    print("\nТаблиця пропорційної заміни")
    for i in range(letter_amount):
        print("\"{}\" ".format(alphabet[i]), end="")
        for element in table[i]:
            print("{} ".format(element), end="")
        print("")
    print("")
    return table


def encrypt(text, alphabet, table):
    result = ""
    for char in text:
        if char in alphabet:
            char_index = alphabet.index(char)

            result += str(table[char_index][random.randint(0, len(table[char_index]) - 1)])
        else:
            result += char
    return result


def decrypt(encrypted_text, alphabet, table):
    index = 0
    result = ""
    while index < len(encrypted_text):
        number = encrypted_text[index: index + 3]
        if number.isdecimal():
            number = int(number)
            for i in range(0, len(table)):
                if number in table[i]:
                    result += alphabet[i]
        else:
            result += number
        index += 3
    return result


def read_input_file(file_name):
    result = ""
    with open(file_name, "r", encoding="utf-8") as f:
        while True:
            line = f.readline()
            if not line:
                break
            result += line
    return result


def main():
    ua_text = read_input_file("input_ua.txt").lower()
    uk_alphabet = " абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
    table = generate_table(uk_alphabet)
    encrypted_text = encrypt(ua_text, uk_alphabet, table)
    decrypted_text = decrypt(encrypted_text, uk_alphabet, table)

    print("Оригінальний текст з файлу українською:")
    print(ua_text)
    print("\nЗашифрований текст українською:")
    print(encrypted_text)
    print("\nДешифрований текст українською:")
    print(decrypted_text)


if __name__ == "__main__":
    main()
