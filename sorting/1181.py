import sys

n = int(sys.stdin.readline().rstrip())
arr = list()
for _ in range(n):
    arr.append(sys.stdin.readline().rstrip().rstrip())
arr = sorted(list(set(arr)))
dic = {}
for n,i in enumerate(arr):
    dic[i] = len(i)
for i in sorted(dic.items(), key=lambda x:x[1]):
    print(i[0])