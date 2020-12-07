def accumulate_answers(file):
    string_list = open(file).readlines()

    answers = []
    cur_answer_grouping = ''
    for i in range(0, len(string_list)):
        cur_line = string_list[i].strip()
        cur_line_unique = list(dict.fromkeys(cur_line))

        if len(cur_line) == 0 or cur_line.isspace():
            answers.append(cur_answer_grouping)
            cur_answer_grouping = ''
        else:
            for char in cur_line_unique:
                if char not in cur_answer_grouping:
                    cur_answer_grouping = cur_answer_grouping + char

        if i == len(string_list) - 1:
            answers.append(cur_answer_grouping)
            cur_answer_grouping = ''

    print('total answers ', len(answers))
    print('last answer ', answers[len(answers) - 1])
    return answers


def count_answers(answer_list):
    count = 0
    for answer in answer_list:
        count = count + len(answer)

    print('total count ', count)
    return count


def summation():
    answers = accumulate_answers('day6-input')
    return count_answers(answers)


def main():
    summation()


main()
