import sys
from collections import deque

s, t = map(int, input().split())

que = deque()
check = set()

que.append((s, ''))
check.add(s)
max = 10e9

if s == t:
    print(0)
else:
    res = -1
    while que:
        cv, cs = que.popleft()
        if cv == t:
            res = cs
            print(res)
            exit(0)

        nv = cv * cv
        if 0 <= nv <= max and nv not in check:
            que.append((nv, cs+'*'))
            check.add(nv)

        nv = cv + cv
        if 0 <= nv <= max and nv not in check:
            que.append((nv, cs+'+'))
            check.add(nv)

        nv = 1
        if nv not in check:
            que.append((nv, cs+'/'))
            check.add(nv)

    print(res)
