import sys

n = int(sys.stdin.readline().rstrip())
arr = list()
for _ in range(n):
    inp = sys.stdin.readline().rstrip().split()
    arr.append([int(inp[0]), inp[1]])
for i in sorted(arr, key=lambda x:x[0]):
    print(i[0],i[1])