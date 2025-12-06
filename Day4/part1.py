def main():
    file = open("Day4/input.txt", "r")
    lines = []
    for line in file:
        lines.append(line.strip())
    file.close()
    findSurrounding(lines)

def findSurrounding(lines):
    total = 0
    i = 0
    while i < len(lines):
        j = 0
        currLine = lines[i]
        while j < len(currLine):
            surrounding = 0
            if currLine[j] == ".":
                j+=1
            else:
                if i > 0:
                    if j > 0 and lines[i-1][j-1] == "@":
                        surrounding += 1
                    if j < len(currLine)-1 and lines[i-1][j+1]=="@":
                        surrounding += 1
                    if lines[i-1][j] == "@":
                        surrounding += 1
                if j > 0:
                    if currLine[j-1] == "@":
                        surrounding += 1
                if j < len(currLine)-1:
                    if currLine[j+1] == "@":
                        surrounding += 1
                if i < len(lines)-1:
                    if j > 0 and lines[i+1][j-1] == "@":
                        surrounding += 1
                    if j < len(currLine)-1 and lines[i+1][j+1]=="@":
                        surrounding += 1
                    if lines[i+1][j] == "@":
                        surrounding += 1
                if surrounding < 4:
                    total += 1
                j+=1
        i+=1
    print(total)
            
if __name__ == "__main__":
    main()