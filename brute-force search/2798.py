import sys
from itertools import combinations

N,M = map(int,sys.stdin.readline().rstrip().split())
arr = list(map(int,sys.stdin.readline().rstrip().split()))

ans = 0
for i in combinations(arr, 3):
    if ((M-sum(i)) < (M-ans))&(sum(i)<=M):
        ans = sum(i)
print(ans)