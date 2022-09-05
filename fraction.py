n = int(input())
x, y = 0, 0
while n > y:
    x += 1
    y += x

if x % 2 == 0:
    up = x - (y-n)
    down = (y-n) + 1
else:
    up = (y-n) + 1
    down = x - (y-n)

print(f'{up}/{down}')
