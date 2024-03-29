n = int(input())
dp = []

for i in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            dp[i][0] = dp[-1][0] + dp[i][0]
        elif i == j:
            dp[i][j] = dp[i-1][j-1] + dp[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1]+dp[i][j], dp[i-1][j] + dp[i][j])

print(max(dp[n-1]))
