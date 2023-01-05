import sys
N = int(sys.stdin.readline().rstrip())

arr = list()
for i in range(666,3000000):
    if '666' in str(i):
        arr.append(i)
print(arr[N-1])