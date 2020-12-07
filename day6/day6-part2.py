def accumulate_answers(file):
    string_list = open(file).readlines()

    answers = []
    cur_answer_grouping = []
    for i in range(0, len(string_list)):
        cur_line = string_list[i].strip()

        if len(cur_line) == 0 or cur_line.isspace():
            answers.append(cur_answer_grouping)
            cur_answer_grouping = []
        else:
            cur_answer_grouping.append(list(cur_line))

        if i == len(string_list) - 1:
            answers.append(cur_answer_grouping)
            cur_answer_grouping = []

    print('total answers ', len(answers))
    print('last answer ', answers[len(answers) - 1])
    return answers


def count_answers(answer_list):
    count = 0
    for answer in answer_list:
        letters_in_all_lists = set(answer[0])
        for l in answer:
            existing_set = set(letters_in_all_lists)
            potential_set = set(l)
            letters_in_all_lists = existing_set.intersection(potential_set)

        count = count + len(letters_in_all_lists)

    print('total count ', count)
    return count


def summation():
    answers = accumulate_answers('day6-input')
    return count_answers(answers)


def main():
    summation()


main()
