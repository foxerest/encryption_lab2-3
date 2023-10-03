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
            return result, False
    return result, True


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


def write_output_file(file_name, text):
    with open(file_name, "w") as f:
        f.write(text)
    f.close()


def create_frequency_tables(alphabet, table, input_text, encrypted_text):
    print("\nТаблиця із частотою символів у відкритому тексті")
    for letter in alphabet:
        print("\"{}\" ".format(letter), end="")
        print("{} ".format(input_text.count(letter)))
    print("\nТаблиця із частотою символів у криптограмі")
    all_symbols = []
    for row in table:
        for symbol in row:
            all_symbols.append(symbol)
    all_symbols.sort()
    for symbol in all_symbols:
        print("\"{}\" ".format(symbol), end="")
        print("{} ".format(encrypted_text.count(str(symbol))))
    print("")


def main():
    input_file_name = "input_ua.txt"
    output_file_name = "output_ua.txt"
    ua_text = read_input_file(input_file_name).lower()
    uk_alphabet = " абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
    table = generate_table(uk_alphabet)
    encrypted_text, encryption_success = encrypt(ua_text, uk_alphabet, table)
    if encryption_success:
        decrypted_text = decrypt(encrypted_text, uk_alphabet, table)

        print("Оригінальний текст з файлу українською:")
        print(ua_text)
        print("\nЗашифрований текст:")
        print(encrypted_text)
        print("\nДешифрований текст:")
        print(decrypted_text)
        write_output_file(output_file_name, decrypted_text)
        print("\nПеревірка правильності кінцевого тексту:")
        if ua_text == decrypted_text:
            print("Оскількі текст однаковий перевірка пройдена!")
        else:
            print("Оскількі текст НЕ однаковий перевірка НЕ пройдена!")
        create_frequency_tables(uk_alphabet, table, ua_text, encrypted_text)
    else:
        print("\nСхоже у тексті, який ви намагаєтесь зашифрувати, присутні некоректні символи."
              "\nДопускається використання лише літер українського алфавіту та пробілів")


if __name__ == "__main__":
    main()
