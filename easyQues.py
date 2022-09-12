a, b = map(int, input().split())
hap = []
for i in range(1, b+1):
    for j in range(i):
        hap.append(i)

print(sum(hap[a-1:b]))
