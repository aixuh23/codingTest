n = int(input())
reserveRoom = []

for i in range(n):
    s, e = map(int, input().split())
    reserveRoom.append([s, e])

reserveRoom = sorted(reserveRoom, key=lambda s: s[0])
reserveRoom = sorted(reserveRoom, key=lambda e: e[1])

time = 0
cntRoom = 0

for i, j in reserveRoom:
    if i >= time:
        cntRoom += 1
        time = j

print(cntRoom)
