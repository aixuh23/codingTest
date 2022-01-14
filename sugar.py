<<<<<<< HEAD
import sys

N = int(input())

num = 0

while True:
    if(N < 0):
        print(-1)
        break
    if((N % 5) == 0):
        num += (N//5)
        print(num)
        break
    N -= 3
    num += 1
=======
import sys

N = int(input())

num = 0

while True:
    if(N < 0):
        print(-1)
        break
    if((N % 5) == 0):
        num += (N//5)
        print(num)
        break
    N -= 3
    num += 1
>>>>>>> 2ce264b9b83f5163c020009011bd654d32901386
