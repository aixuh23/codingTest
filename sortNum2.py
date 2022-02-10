import sys
n = int(input())
num = []
for i in range(n):
    num.append(int(sys.stdin.readline()))

sortedNum = sorted(num)

for i in sortedNum:
    sys.stdout.write(str(i) + "\n")

# pypy3
# n = int(input())

# num = []

# for i in range(n):
#     num.append(int(input()))

# sortedNum = sorted(num)

# for j in range(len(sortedNum)):
#     print(sortedNum[j])
