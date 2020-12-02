def calculate(file):
    string_list = open(file).readlines()

    for string1 in string_list:
        for string2 in string_list:
            for string3 in string_list:
                number1 = int(string1.rstrip())
                number2 = int(string2.rstrip())
                number3 = int(string3.rstrip())
                if number1 + number2 + number3 == 2020:
                    product = number1 * number2 * number3
                    print('Multiplied %s, %s, %s to get %s', (number1, number2, number3, product))


def main():
    calculate("day1-input")


main()
