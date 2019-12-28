#!/usr/bin/env python3


basecode = [1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 10, 1, 19, 1, 19, 6, 23, 2, 13, 23, 27, 1, 27, 13, 31, 1, 9,
        31, 35, 1, 35, 9, 39, 1, 39, 5, 43, 2, 6, 43, 47, 1, 47, 6, 51, 2, 51, 9, 55, 2, 55, 13, 59, 1, 59, 6, 63, 1,
        10, 63, 67, 2, 67, 9, 71, 2, 6, 71, 75, 1, 75, 5, 79, 2, 79, 10, 83, 1, 5, 83, 87, 2, 9, 87, 91, 1, 5, 91, 95,
        2, 13, 95, 99, 1, 99, 10, 103, 1, 103, 2, 107, 1, 107, 6, 0, 99, 2, 14, 0, 0]


"""
code=[1,0,0,0,99]
code=[2,3,0,3,99]
code=[1,1,1,4,99,5,6,0,99]
"""


def process(code):
    step = 0
    while code[step] != 99:
        if code[step] == 1:
            code[code[step+3]] = code[code[step+1]] + code[code[step+2]]
        elif code[step] == 2:
            code[code[step+3]] = code[code[step+1]] * code[code[step+2]]
        else:
            print('invalid intcode', 'step:',step, 'code:', code[step])
        step += 4
    return code


def process_to (noun, verb):
    code = basecode.copy()
    code[1] = noun
    code[2] = verb
    process(code)
    return code


def get_result(result):
    noun = 0
    verb = 0
    code = [0]
    for noun in range(0, 100):
        for verb in range(0, 100):
            code = process_to(noun, verb)
            if code[0] == result:
                return code


if __name__ == '__main__':
    code = get_result(19690720)

    for value in code:
        print(value, end=",")
    print()
    print('init:', str(code[1]) + str(code[2]))
