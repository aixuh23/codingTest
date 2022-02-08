n, k = map(int, input().split(" "))
nList = list(map(int, input().split()))

temp = 0
sum = 0
MaxSum = 0

for i in range(len(nList)-k+1):
    sum += nList[i]
    if i-temp+1 == k:
        MaxSum = max(MaxSum, sum)
        sum -= nList[temp]
        temp += 1
print(MaxSum)

# temp = sum(nList[:k])
# MaxSum = temp

# for i in range(k, len(nList)-k+1):
#     temp += nList[i] - nList[i-k]
#     MaxSum = max(MaxSum, temp)

# print(MaxSum)
