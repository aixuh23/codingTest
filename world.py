n = input().upper()
world = list(set(n))

cnt = []
for i in world:
    count = n.count
    cnt.append(count(i))

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(world[(cnt.index(max(cnt)))])
