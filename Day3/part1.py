with open("Day3\\input.txt") as f:
  sum = 0
  for x in f:
    x = x.strip()
    firstBattery = "0"
    firstIdx = 0
    idx = 0
    while idx < len(x)-1:
      if int(x[idx]) > int(firstBattery):
        firstBattery = x[idx]
        firstIdx = idx
      idx+=1
    secondBattery = "0"
    idx = firstIdx+1
    while idx < len(x):
      if int(x[idx]) > int(secondBattery):
        secondBattery = x[idx]
      idx += 1
    print(firstBattery+secondBattery)
    sum += int(firstBattery+secondBattery)
print(sum)