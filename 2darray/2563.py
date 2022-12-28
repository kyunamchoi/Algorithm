N = int(input())
row, col = 100, 100
Mat = [[0] * col for _ in range(row)]

for n in range(N):
    x,y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            Mat[y+i][x+j] += 1

total = 0
for i in range(100):
    for j in range(100):
        if Mat[i][j] > 0:
            total += 1

print(total)