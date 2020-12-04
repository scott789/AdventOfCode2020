class Passport:
    def __init__(self, parts=None):
        if parts is None:
            parts = {}
        self.parts = parts


def accumulate_passports(file):
    string_list = open(file).readlines()

    passports = []
    cur_passport = Passport()
    for i in range(0, len(string_list)):
        cur_line = string_list[i].strip()
        cur_line_pieces = cur_line.split(' ')

        if cur_line.isspace() or len(cur_line) == 0:
            passports.append(cur_passport)
            cur_passport = Passport()
        else:
            for piece in cur_line_pieces:
                pair = piece.split(':')
                key = pair[0]
                val = pair[1]
                cur_dict = cur_passport.parts
                cur_dict[key] = val
                cur_passport = Passport(cur_dict)

    print('total passports ', len(passports))
    return passports


def filter_passports(passports, keys):
    for passport in passports:
        if all(key in passport.parts for key in keys):
            yield passport


def summation():
    total_passports = accumulate_passports('day4-input')
    valid_passports = filter_passports(total_passports, ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    return sum(1 for x in valid_passports)


def main():
    print('total valid passports ', summation())


main()
