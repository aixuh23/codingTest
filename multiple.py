n = list(map(int, input().split()))
mul = min(n)
while True:
    cnt = 0
    for i in n:
        if mul % i == 0:
            cnt += 1
    if cnt >= 3:
        break
    mul += 1
print(mul)
