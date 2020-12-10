def clean_string(line):
    return int(line.strip())


def adapter_can_accept_joltages(adapter_rating, hot_wire_joltages):
    return adapter_rating - hot_wire_joltages <= 3


def get_next_adapter(adapters, floor_joltage):
    for i in range(3):
        if adapter_can_accept_joltages(adapters[i], floor_joltage):
            return adapters[i]
    return 'Failure'


def get_jolted(file, initial_joltage):
    string_list = open(file).readlines()
    num_list = list(map(clean_string, string_list))
    num_list.sort()

    built_in_limit = num_list[len(num_list) - 1] + 3
    num_one = 0
    num_two = 0
    num_three = 0

    initial_jump = num_list[0] - initial_joltage
    if initial_jump == 1:
        num_one = num_one + 1
    elif initial_jump == 2:
        num_two = num_two + 1
    elif initial_jump == 3:
        num_three = num_three + 1
    else:
        return 'ERROR 1'

    for i in range(len(num_list)):
        cur = num_list[i]
        nxt = built_in_limit if i == len(num_list) - 1 else num_list[i + 1]

        if nxt - cur == 1:
            num_one = num_one + 1
        elif nxt - cur == 2:
            num_two = num_two + 1
        elif nxt - cur == 3:
            num_three = num_three + 1
        else:
            return 'ERROR 2'

    return [num_one, num_two, num_three]


def main():
    result = get_jolted('day10-input', 0)
    print('result ', result)
    print('answer1 ', result[0] * result[2])


main()
