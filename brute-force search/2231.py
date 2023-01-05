import sys
N = int(sys.stdin.readline().rstrip())
ans = 0
for i in range(N):
    x = i
    for j in range(len(str(i))):
        x += int(str(i)[j])
    if x == N:
        ans = i
        break
print(ans)