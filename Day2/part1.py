def main():
    file = open("Day2/day2.txt", "r")
    line = file.readline()
    ranges = line.split(',')
    sum = 0
    for range in ranges:
        range = range.split('-')
        min = int(range[0])
        max = int(range[1])
        while min <= max:
            if len(range[0]) % 2 != 0:
                min += 1
                continue
            else:
                stringMin = str(min)
                firstHalf = stringMin[0:len(stringMin)//2]
                secondHalf = stringMin[len(stringMin)//2:len(stringMin)]
                if firstHalf == secondHalf:
                    sum += min
            min += 1
    print(sum)
    file.close()

if __name__ == "__main__":
    main()