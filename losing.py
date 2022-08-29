n = input().split("-")
res = 0
for i in n[0].split("+"):
    res += int(i)
for i in n[1:]:
    for j in i.split("+"):
        res -= int(j)
print(res)
# 마이너스 기호를 만날 때 다음 마이너스까지,
# if 마이너스가 없다면, 끝까지 모든 수를 더해서 한번에 빼주면 되는 문제
