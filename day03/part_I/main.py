import json

scores = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13,
          "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25,
          "z": 26, "A": 27, "B": 28, "C": 29, "D": 30, "E": 31, "F": 32, "G": 33, "H": 34, "I": 35, "J": 36, "K": 37,
          "L": 38, "M": 39, "N": 40, "O": 41, "P": 42, "Q": 43, "R": 44, "S": 45, "T": 46, "U": 47, "V": 48, "W": 49,
          "X": 50, "Y": 51, "Z": 52}

json_score = json.dumps(scores)
score = 0
group_counter = 0
# open input file
with open('input_test.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()

    # loop through lines and add every line to score
    for line in lines:

        # get length of line
        x = len(line)

        # make 2 strings from one line, split by half
        compartment1 = slice(0, len(line) // 2)
        compartment2 = slice(len(line) // 2, len(line))

        # compare 2 strings
        a = list(set(line[compartment1]) & set(line[compartment2]))
        for i in a:
            if i in json_score:
                resp = json.loads(json_score)

                # look in json for value of char and add to score
                score += resp[i]

    print(score)
