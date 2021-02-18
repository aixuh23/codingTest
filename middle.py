"""import sys
import heapq

left, right = [], []

N = int(input())

for _ in range(N):
    Nn = int(input())
    if(len(left) == len(right)):
        heapq.heappush(left, (-Nn, Nn))
        print(left[0][1])
    else:
        heapq.heappush(right, (Nn, Nn))
        print(left[0][1])

    if right and left[0][1] > right[0][1]:
        left_v = heapq.heappop(left)[1]
        right_v = heapq.heappop(right)[1]
        heapq.heappush(right, (left_v, left_v))
        heapq.heappush(left, (-right_v, right_v))
"""
# print(left[0][1])
###

import sys
from bisect import bisect_left

if __name__ == "__main__":
    N = int(input())  # 외칠 개수
    arr = []

    Nn = int(input())  # 입력할 숫자
    arr.append(Nn)

    length = 1

    for _ in range(N-1):
        Nn = int(input())
        index = bisect_left(arr, Nn)
        arr.insert(index, Nn)
        length += 1

        if((length % 2) == 0):
            print(min(arr[length // 2 - 1], arr[length // 2]))
        else:
            print((arr[length // 2]))
