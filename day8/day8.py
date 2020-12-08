class Instruction:
    def __init__(self, ins, addr):
        self.addr = addr
        self.ins = ins


def retrieve_ins(raw_list):
    ret = []
    for row in raw_list:
        stripped = row.strip()
        split = stripped.split(' ')
        if split[1][0] == '+':
            address = int(split[1][1:])
        else:
            address = int(split[1][1:]) * -1

        ret.append(Instruction(split[0], address))
    return ret


def find_loop(instructions, cur_ix, indices_reached, accumulator):
    print('cur ix ', cur_ix)

    if len(indices_reached) > 0:
        if cur_ix in indices_reached:
            return accumulator

    instruction = instructions[cur_ix]

    if instruction.ins == 'nop':
        next_ix = cur_ix + 1
        indices_reached.append(cur_ix)
        return find_loop(instructions, next_ix, indices_reached, accumulator)
    elif instruction.ins == 'acc':
        next_ix = cur_ix + 1
        new_acc = accumulator + instruction.addr
        indices_reached.append(cur_ix)
        return find_loop(instructions, next_ix, indices_reached, new_acc)
    elif instruction.ins == 'jmp':
        next_ix = cur_ix + instruction.addr
        indices_reached.append(cur_ix)
        return find_loop(instructions, next_ix, indices_reached, accumulator)


def boot_up(file):
    string_list = open(file).readlines()
    instructions = retrieve_ins(string_list)

    acc = find_loop(instructions, 0, [], 0)
    print('acc ', acc)
    return acc


def main():
    boot_up('day8-input')


main()
