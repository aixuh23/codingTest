n = int(input())
student_info = []

for _ in range(n):
    weight, height = list(map(int, input().split(" ")))
    student_info.append((weight, height))

for i in student_info:
    rank = 1
    for j in student_info:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')
