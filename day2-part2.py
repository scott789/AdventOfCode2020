def calculate(file):
    string_list = open(file).readlines()

    valid_passwords = 0
    invalid_passwords = 0

    for line in string_list:
        split_result = line.split('-')
        char_loc_1 = int(split_result[0])
        char_loc_2 = int(split_result[1].split(' ')[0])
        character = split_result[1].split(' ')[1].split(':')[0]
        password = split_result[1].split(' ')[2]

        char1 = password[char_loc_1 - 1]
        char2 = password[char_loc_2 - 1]
        if ((char1 == character) and (char2 != character)) or ((char1 != character) and (char2 == character)):
            valid_passwords += 1
        else:
            invalid_passwords += 1

    print('valid passwords: ', valid_passwords)
    print('invalid passwords: ', invalid_passwords)


def main():
    calculate("day2-input")


main()
