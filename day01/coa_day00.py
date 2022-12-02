# define variables
lineCount = 0 firstLine = True result = 0
# open input file
with open('input.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    # loop thru lines
    for line in lines:
        # check for empty line (empty line means end of deer)
        if line in ['\n', '\r', '\r\n']:
            # print result, reset first line and result counter
            print(result)
            firstLine = True
            result = 0
        else:
            # if first line, set line value to result var
            if firstLine:
                result = int(line)
            else:
                # if additional line, add line value to result
                result += int(line)
            # after first line, set firstline to false
            firstLine = False
