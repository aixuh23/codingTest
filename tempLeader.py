n = int(input())
classes = []
equal = [0] * n

for i in range(n):
    classes.append(list(map(int, input().split())))
    equal[i] = [0]*n

for i in range(5):
    for j in range(n):
        for k in range(j+1, n):
            if classes[j][i] == classes[k][i]:
                equal[k][j] = 1
                equal[j][k] = 1

cnt = []
for l in equal:
    cnt.append(l.count(1))

print(cnt.index(max(cnt))+1)
