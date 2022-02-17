import sys


def countNum(Narray, m, start, end):
    if start > end:
        return False

    mid = (start + end) // 2
    if (Narray[mid] == m):
        return True
    elif (Narray[mid] > m):
        return countNum(Narray, m, start, mid-1)
    else:
        return countNum(Narray, m, mid+1, end)


N = int(input())
Narray = sorted(list(map(int, input().split())))
M = int(input())
Marray = list(map(int, input().split()))

for M in Marray:
    if(countNum(Narray, M, 0, N-1)):
        print(1)
    else:
        print(0)
#####


def countNum(Narray, m, start, end):
    if start > end:
        return False

    mid = (start + end) // 2
    if (Narray[mid] == m):
        return True
    elif (Narray[mid] > m):
        return countNum(Narray, m, start, mid-1)
    else:
        return countNum(Narray, m, mid+1, end)


N = int(input())
Narray = sorted(list(map(int, input().split())))
M = int(input())
Marray = list(map(int, input().split()))

for M in Marray:
    if(countNum(Narray, M, 0, N-1)):
        print(1)
    else:
        print(0)
