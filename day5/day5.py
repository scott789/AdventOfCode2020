class Recurse:
    def __init__(self, chars, max_row, min_row, max_col, min_col):
        self.min_col = min_col
        self.max_col = max_col
        self.chars = chars
        self.min_row = min_row
        self.max_row = max_row


def get_location(recurse):
    print('recurse ', recurse.chars)

    if len(recurse.chars) == 0:
        return recurse

    first_char = recurse.chars[0]

    if len(recurse.chars) == 4:
        if first_char == 'F':
            return get_location(
                Recurse(recurse.chars[1:], recurse.min_row, recurse.min_row, recurse.max_col, recurse.min_col))
        elif first_char == 'B':
            return get_location(
                Recurse(recurse.chars[1:], recurse.max_row, recurse.max_row, recurse.max_col, recurse.min_col))

    if len(recurse.chars) == 1:
        if first_char == 'L':
            return get_location(
                Recurse(recurse.chars[1:], recurse.max_row, recurse.min_row, recurse.min_col, recurse.min_col))
        if first_char == 'R':
            return get_location(
                Recurse(recurse.chars[1:], recurse.max_row, recurse.min_row, recurse.max_col, recurse.max_col))

    if first_char == 'F':
        max_row = recurse.max_row - ((recurse.max_row - recurse.min_row) // 2 + 1)
        return get_location(
            Recurse(recurse.chars[1:], max_row, recurse.min_row, recurse.max_col, recurse.min_col))
    elif first_char == 'B':
        min_row = recurse.min_row + (recurse.max_row - recurse.min_row) // 2 + 1
        return get_location(
            Recurse(recurse.chars[1:], recurse.max_row, min_row, recurse.max_col, recurse.min_col))
    elif first_char == 'L':
        max_col = recurse.max_col - ((recurse.max_col - recurse.min_col) // 2 + 1)
        return get_location(
            Recurse(recurse.chars[1:], recurse.max_row, recurse.min_row, max_col, recurse.min_col))
    elif first_char == 'R':
        min_col = recurse.min_col + (recurse.max_col - recurse.min_col) // 2 + 1
        return get_location(
            Recurse(recurse.chars[1:], recurse.max_row, recurse.min_row, recurse.max_col, min_col))


def fetch_seat_id(seat_id, recurse):
    if len(seat_id) > 0:
        result_rescurse = get_location(recurse)
        print('recurse for ', result_rescurse.chars)
        return result_rescurse


def fetch_seat_ids(file):
    string_list = open(file).readlines()
    seats = []
    for row in string_list:
        cur_line = row.strip()
        print('cur_line ', cur_line)
        seat = fetch_seat_id(cur_line, Recurse(cur_line, 127, 0, 7, 0))
        seats.append(seat)

    return seats


def main():
    seat_locations = fetch_seat_ids('day5-input')
    # count_seats = sum(1 for x in seat_locations)
    print('seat ids ', seat_locations)

    max_seat_id = 0
    for seat in seat_locations:
        seat_id = seat.max_row * 8 + seat.max_col
        if seat_id > max_seat_id:
            max_seat_id = seat_id

    print('max seat id ', max_seat_id)


main()
