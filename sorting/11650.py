import sys

n = int(sys.stdin.readline().rstrip())
arr = list()
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))
for i in sorted(arr):
    print(i[0],i[1])