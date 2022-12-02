# opponent (left column)
# A = rock
# B = paper
# C = scissors

# response (right column)
# X = rock
# Y = paper
# Z = scissors

# points for response
# X (rock) = 1
# Y (paper) = 2
# Z (scissors) = 3

# points for result
# 0 = lost
# 3 = draw
# 6 = won

score = 0


def get_result(left, right):
    # lost
    if left == 'A' and right == 'Z' or left == 'B' and right == 'X' or left == 'C' and right == 'Y':
        single_score = 0

    # draw
    if left == 'A' and right == 'X' or left == 'B' and right == 'Y' or left == 'C' and right == 'Z':
        single_score = 3

    # won
    if left == 'A' and right == 'Y' or left == 'B' and right == 'Z' or left == 'C' and right == 'X':
        single_score = 6

    # points for choosen sign
    if right == 'X':
        single_score += 1
    elif right == 'Y':
        single_score += 2
    elif right == 'Z':
        single_score += 3

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
