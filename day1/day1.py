def calculate(file):
    string_list = open(file).readlines()

    for string1 in string_list:
        for string2 in string_list:
            number1 = int(string1.rstrip())
            number2 = int(string2.rstrip())
            if number1 + number2 == 2020:
                print('Multiplied ', number1 * number2)


def main():
    calculate("day1-input")


main()
