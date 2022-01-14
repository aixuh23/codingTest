n = int(input())

num = []

for i in range(n):
    num.append(int(input()))

sortedNum = sorted(num)

for i in range(len(sortedNum)):
    print(sortedNum[i])
