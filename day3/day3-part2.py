def calculate(file, x_increment, y_increment):
    string_list = open(file).readlines()

    max_width = len(string_list[0].strip())
    max_height = len(string_list)
    trees_count = 0

    x = 0
    for y in range(0, max_height, y_increment):
        cur_line = string_list[y].strip()
        cur_char = cur_line[x]
        if cur_char == '#':
            trees_count += 1
        x += x_increment
        x = x % max_width

    print('trees: ', trees_count)
    return trees_count


def aggregate():
    trees1 = calculate("day3-input", 1, 1)
    trees2 = calculate("day3-input", 3, 1)
    trees3 = calculate("day3-input", 5, 1)
    trees4 = calculate("day3-input", 7, 1)
    trees5 = calculate("day3-input", 1, 2)
    print('trees ', trees1, trees2, trees3, trees4, trees5)

    return trees1 * trees2 * trees3 * trees4 * trees5


def main():
    print('Product ', aggregate())


main()
