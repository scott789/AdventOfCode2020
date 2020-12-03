def calculate(file):
    string_list = open(file).readlines()

    max_width = len(string_list[0].strip())
    max_height = len(string_list)
    trees_count = 0

    x = 0
    for y in range(0, max_height, 1):
        cur_line = string_list[y].strip()
        cur_char = cur_line[x]
        if cur_char == '#':
            trees_count += 1
        x += 3
        x = x % max_width

    print('trees: ', trees_count)


def main():
    calculate("day3-input")


main()
