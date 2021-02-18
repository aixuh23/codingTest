import sys

N = int(input())  # 5
Pn = list(map(int, input().split()))  # 3 1 4 3 2

Pn.sort()  # 1 2 3 3 4

time = 0

for i in range(N):
    for j in range(i+1):
        time += Pn[j]

print(time)
