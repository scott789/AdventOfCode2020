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


def filter_required_fields_present(passports, keys):
    for passport in passports:
        if all(key in passport.parts for key in keys):
            yield passport


def filter_valid_fields(passports):
    for passport in passports:
        byr = passport.parts['byr']
        if len(byr) == 4 and 1920 <= int(byr) <= 2002:
            pass
        else:
            continue

        iyr = passport.parts['iyr']
        if len(iyr) == 4 and 2010 <= int(iyr) <= 2020:
            pass
        else:
            continue

        eyr = passport.parts['eyr']
        if len(eyr) == 4 and 2020 <= int(eyr) <= 2030:
            pass
        else:
            continue

        hgt = passport.parts['hgt']
        # hgt_digits = [int(i) for i in hgt.split() if i.isdigit()]
        hgt_digits = ''
        for char in hgt:
            if char.isdigit():
                hgt_digits += char
        # hgt_letters = [int(i) for i in hgt.split() if i.isalpha()]
        hgt_letters = ''
        for char in hgt:
            if char.isalpha():
                hgt_letters += char
        if hgt_letters == 'cm' and 150 <= int(hgt_digits) <= 193:
            pass
        elif hgt_letters == 'in' and 59 <= int(hgt_digits) <= 76:
            pass
        else:
            continue

        hcl = passport.parts['hcl']
        if len(hcl) == 7 and hcl[0] == '#':
            hcl_alnum = hcl[1:]
            if hcl_alnum.isalnum():
                pass
            else:
                continue
        else:
            continue

        ecl = passport.parts['ecl']
        if ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            pass
        else:
            continue

        pid = passport.parts['pid']
        if len(pid) == 9 and pid.isdigit():
            pass
        else:
            continue

        yield passport


def summation():
    total_passports = accumulate_passports('day4-input')
    all_fields_present_passports = filter_required_fields_present(total_passports,
                                                                  ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    all_present_fields_valid_passports = filter_valid_fields(all_fields_present_passports)
    return sum(1 for x in all_present_fields_valid_passports)


def main():
    print('total valid passports ', summation())


main()
