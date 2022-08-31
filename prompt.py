n = int(input())
fileName = list(input())
fileLength = len(fileName)

for i in range(n-1):
    fileName2 = list(input())
    for j in range(fileLength):
        if fileName[j] != fileName2[j]:
            fileName[j] = '?'
print(''.join(fileName))
