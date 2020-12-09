def clean_string(line):
    return int(line.strip())


def contiguous_sum(target, num_list):
    return sum(num_list) == target


def decipher(file, number_to_sum_to):
    string_list = open(file).readlines()
    num_list = list(map(clean_string, string_list))

    for i in range(len(num_list)):
        for j in range(i + 1, len(num_list)):
            current_corpus = num_list[i: j]
            if contiguous_sum(number_to_sum_to, current_corpus):
                return current_corpus

    return 'Not found'


def main():
    result = decipher('day9-input', 26796446)
    # result = decipher('day9-input-debug', 127)
    print('result ', min(result) + max(result))


main()
