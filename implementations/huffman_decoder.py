"""
Восстановите строку по её коду и беспрефиксному коду символов.
В первой строке выходного файла выведите строку 𝑠. Она должна состоять из
строчных букв латинского алфавита. Гарантируется, что длина правильного
ответа не превосходит 104 символов.
"""


def main():
    n_sym = int(input().split()[0])
    codes = [input().split(": ") for _ in range(n_sym)]
    string_enc = input()

    string_dec = ""

    while string_enc:
        for i in codes:
            if string_enc.startswith(i[1]):
                string_enc = string_enc[len(i[1]):]
                string_dec += i[0]
            else:
                continue

    print(string_dec)


if __name__ == '__main__':
    main()



