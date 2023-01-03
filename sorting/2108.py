import sys
from collections import Counter

n = int(sys.stdin.readline().rstrip())
arr = list()
for _ in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))

print(round(sum(arr)/len(arr)))
print(sorted(arr)[len(arr)//2])

cnt = Counter(sorted(arr)).most_common(2)

if len(cnt) > 1:
    if cnt[0][1]==cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
    
print(max(arr)-min(arr))