from re import L
import sys
n, m = map(int, sys.stdin.readline().split(" "))
data = []


def solve():
    if len(data) == m:
        print(' '.join(map(str, data)))
        return

    for i in range(1, n+1):
        if i in data:
            continue
        data.append(i)
        solve()
        data.pop()


solve()

# from itertools import permutations
# N, M = map(int, input().split())
# P = permutations(range(1, N+1), M)
# for i in P:
#     print(' '.join(map(str, i)))
