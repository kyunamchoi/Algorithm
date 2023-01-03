import sys

n = int(sys.stdin.readline().rstrip())
arr = list()
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))
arr.sort()
for i in sorted(arr, key=lambda x:x[1]):
    print(i[0],i[1])