import sys

N, K = map(int, input().split())

A = [int(input()) for _ in range(N)]

min = 0

A.sort(reverse=True)

for i in A:
    if K == 0:
        break
    min += K//i
    K %= i

print(min)
