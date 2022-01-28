n = int(input())
room = 1
move = 6
cnt = 1

while n > room:
    room += move
    cnt += 1
    move += 6
print(cnt)

# while n > room:
#     room += 6 * cnt
#     cnt += 1

# print(cnt)
