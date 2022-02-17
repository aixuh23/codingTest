n, k = map(int, input().split(" "))

a = [int(input()) for _ in range(n)]

a.sort(reverse=True)

coin = 0

for i in a:
    if k == 0:
        break
    coin += k//i
    k %= i
print(coin)
