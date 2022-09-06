# n, m = map(int, input().split())
# castle = []

# for _ in range(n):
#     castle.append(input())

# x, y = 0, 0

# for i in range(n):
#     if "X" not in castle[i]:
#         x += 1

# for j in range(m):
#     if "X" not in [castle[i][j] for i in range(n)]:
#         y += 1

# print(max(x, y))


n, m = map(int, input().split())
castle = []

for _ in range(n):
    castle.append(input())

row = [0] * n
column = [0] * m

for i in range(n):
    for j in range(m):
        if castle[i][j] == 'X':
            row[i] = 1
            # print("row: "f'{row}')
            column[j] = 1
            # print("column:" f'{column}')

row_count = 0
for i in range(n):
    if row[i] == 0:
        row_count += 1
        # print("row_count: "f'{row_count}')

column_count = 0
for j in range(m):
    if column[j] == 0:
        column_count += 1
        # print("col_count: "f'{column_count}')

print(max(row_count, column_count))
