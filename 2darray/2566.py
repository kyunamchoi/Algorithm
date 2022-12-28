N,M = 9 ,9
Mat = []
for i in range(N):
    line = list(map(int,input().split()))
    Mat.append(line)

max_val = 0
for i in range(N):
    if max(Mat[i]) >= max_val:
        max_val = max(Mat[i])
        row = i
        col = Mat[i].index(max_val)

print(max_val)
print(row+1, col+1)

