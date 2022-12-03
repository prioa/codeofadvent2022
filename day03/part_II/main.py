import json

scores = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13,
          "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25,
          "z": 26, "A": 27, "B": 28, "C": 29, "D": 30, "E": 31, "F": 32, "G": 33, "H": 34, "I": 35, "J": 36, "K": 37,
          "L": 38, "M": 39, "N": 40, "O": 41, "P": 42, "Q": 43, "R": 44, "S": 45, "T": 46, "U": 47, "V": 48, "W": 49,
          "X": 50, "Y": 51, "Z": 52}

json_score = json.dumps(scores)
score = 0

group_counter = 1
group_str = ""

# open input file
with open('input.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()

    # loop through lines and add every line to score
    for line in lines:
        if group_counter == 3:
            group_str += line
            group_counter = 1

            # split string of 3 by newline
            splitted = group_str.splitlines()

            # search same chars in the strings
            a = list(set(splitted[0]) & set(splitted[1]) & set(splitted[2]))
            for i in a:
                if i in json_score:
                    # look for value of the char in the json
                    resp = json.loads(json_score)
                    # add value to the score var
                    score += resp[i]
            # reset group str for the next 3 lines of the file
            group_str = ""
        else:
            # concatenate lines
            group_str += line
            group_counter += 1

    print(score)
