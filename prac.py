### 음계
# a = list(map(int, input().split(" ")))

# ascending = True
# descending = True

# for i in range(1, 8):
#     if a[i] > a[i - 1]:
#         descending = False
#     elif a[i] < a[i - 1]:
#         ascending = False

# if ascending:
#     print("ascending")
# elif descending:
#     print("descending")
# else:
#     print("mixed")

### 블랙잭
# n, m = list(map(int, input().split(" ")))
# cards = list(map(int, input().split(" ")))

# res = 0
# cnt = 0
# length = len(cards)

# for i in range(0, length):
#     for j in range(i + 1, length):
#         for k in range(j + 1, length):
#             sum = cards[i] + cards[j] + cards[k]
#         if sum <= m:
#             res = max(res, sum)

# print(res)

###스택 수열
# n = int(input())

# cnt = 1
# stack = []
# res = []

# for i in range(1, n + 1):
#     data = int(input())
#     while cnt <= data:
#         stack.append(cnt)
#         cnt += 1
#         res.append("+")
#     if stack[-1] == data:
#         stack.pop()
#         res.append("-")
#     else:
#         print("NO")
#         exit(0)
# print("\n".join(res))

###프린터 큐
# test_case = int(input())
# for _ in range(test_case):
#     n, m = list(map(int, input().split(" ")))
#     que = list(map(int, input().split(" ")))
#     que = [(i, idx) for idx, i in enumerate(que)]
#     cnt = 0

# while True:
#     if que[0][0] == max(que, key=lambda x: x[0])[0]:
#         cnt += 1
#         if que[0][1] == m:
#             print(cnt)
#             break
#         else:
#             que.pop(0)
#     else:
#         que.append(que.pop(0))

### 수 정렬하기
# n = int(input())

# data = []

# for _ in range(n):
#     data.append(int(input()))
# data.sort()

# for x in data:
#     print(x)

### 나이순 정렬
# n = int(input())

# array = []
# for _ in range(n):
#     data = input().split(" ")
#     array.append((int[data[0]], data[1]))

# array = sorted(array, key=lambda x: x[0])

# for i in array:
#     print(i[0], i[1])

### Z
# def solve(n, x, y):
#     global result
#     if n == 2:
#         if x == X and y == Y:
#             print(result)
#             return
#         result += 1
#         if x == X and y + 1 == Y:
#             print(result)
#             return
#         result += 1
#         if x + 1 == X and y == Y:
#             print(result)
#             return
#         result += 1
#         if x + 1 == X and y + 1 == Y:
#             print(result)
#             return
#         result += 1
#         return
#     solve(n / 2, x, y)
#     solve(n / 2, x, y + n / 2)
#     solve(n / 2, x + n / 2, y)
#     solve(n / 2, x + n / 2, y + n / 2)

# result = 0
# N, X, Y = map(int, input().split(' '))
# solve(2 ** N, 0, 0)
