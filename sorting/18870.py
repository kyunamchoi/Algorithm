import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int,sys.stdin.readline().rstrip().split()))
idx = sorted(list(set(arr)))
dic = {}
for n,i in enumerate(idx):
    dic[i] = n
for i in arr:
    print(dic[i],end=' ')