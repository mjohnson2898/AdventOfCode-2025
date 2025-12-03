def main():
    file = open("Day1/day1.txt", "r")
    curr = 50
    zeroCount = 0
    for line in file:
        line = line.strip()
        direction = line[0]
        value = int(line[1:len(line)])
        
        if direction == 'R':
            curr = (curr+value)%100
        else:
            value = value % 100
            curr = (curr-value)
            if curr < 0:
                curr += 100
        if curr == 0:
            zeroCount += 1
    print(zeroCount)
    file.close()

if __name__ == "__main__":
    main()