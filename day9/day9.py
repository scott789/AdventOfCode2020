def clean_string(line):
    return int(line.strip())


def num_in_list(target, num_list):
    found = False
    for i in range(len(num_list)):
        for j in range(i + 1, len(num_list)):
            if num_list[i] + num_list[j] == target:
                found = True

    return found


def decipher(file, preamble_length):
    string_list = open(file).readlines()
    num_list = list(map(clean_string, string_list))

    for i in range(len(num_list)):
        current_corpus = num_list[i: i + preamble_length]
        cur_target = num_list[i + preamble_length]
        if not num_in_list(cur_target, current_corpus):
            return cur_target


def main():
    result = decipher('day9-input', 25)
    print('result ', result)


main()
