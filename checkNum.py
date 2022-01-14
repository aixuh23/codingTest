import math

myNum = list(map(int, input().split(" ")))

temp1 = int(math.pow(myNum[0], 2) + math.pow(myNum[1], 2) +
            math.pow(myNum[2], 2) + math.pow(myNum[3], 2) + math.pow(myNum[4], 2))

print(temp1 % 10)
#lastNum = temp1 % 10
# myNum.append(lastNum)
# print(myNum)
