def calculate(file):
    string_list = open(file).readlines()

    valid_passwords = 0
    invalid_passwords = 0

    for line in string_list:
        split_result = line.split('-')
        minimum_occurrences = int(split_result[0])
        maximum_occurrences = int(split_result[1].split(' ')[0])
        character = split_result[1].split(' ')[1].split(':')[0]
        password = split_result[1].split(' ')[2]

        if (password.count(character) >= minimum_occurrences) and (password.count(character) <= maximum_occurrences):
            valid_passwords += 1
        else:
            invalid_passwords += 1

    print('valid passwords: ', valid_passwords)
    print('invalid passwords: ', invalid_passwords)


def main():
    calculate("day2-input")


main()
