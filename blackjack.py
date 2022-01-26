from tkinter.messagebox import RETRY


n, m = map(int, input().split(" "))
cards = list(map(int, input().split(" ")))

res = 0
for i in range(len(cards)):
    for j in range(i+1, len(cards)):
        for k in range(j+1, len(cards)):
            hap = cards[i] + cards[j] + cards[k]
            if hap <= m:
                res = max(hap, res)
print(res)
