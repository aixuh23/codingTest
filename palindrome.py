while(True):
    n = input()
    copyN = "".join(reversed(n))
    if n == "0":
        break
    if n == copyN:
        print("yes")
    else:
        print("no")
