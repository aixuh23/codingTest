import sys
n = int(input())
arr = []

for i in range(n):
    arr.append(str(sys.stdin.readline().rstrip()))

set_arr = list(set(arr))
set_arr.sort()
set_arr.sort(key=len)

for i in set_arr:
    print(i)
