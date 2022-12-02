score = 0


def get_result(left, right):
    # lost
    if right == 'X':
        single_score = 0
        if left == 'A':
            single_score += 3
        elif left == 'B':
            single_score += 1
        elif left == 'C':
            single_score += 2

    # draw
    if right == 'Y':
        single_score = 3
        if left == 'A':
            single_score += 1
        elif left == 'B':
            single_score += 2
        elif left == 'C':
            single_score += 3

    # won
    if right == 'Z':
        single_score = 6
        if left == 'A':
            single_score += 2
        elif left == 'B':
            single_score += 3
        elif left == 'C':
            single_score += 1

    return single_score


# open input file
with open('input.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()

    # loop thru lines and add every line to score
    for line in lines:
        column = line.split()
        score += get_result(column[0], column[1])

    # print score at the end of the input file
    print(score)
