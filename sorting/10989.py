import sys
n = int(sys.stdin.readline().rstrip())
count = [0] * 10001

for i in range(n):
    num = int(sys.stdin.readline().rstrip())
    count[num] += 1
for i in range(10001):
    for _ in range(count[i]):
        print(i)
#######################################################
"""
같은 알고리즘을 사용하더라도 arr를 만들고, append 하는 과정을 최소로. 메모리 사용 down
"""
#######################################################
def counting_sort(arr):
    max_arr = 10000
    count = [0] * (max_arr+1)
    sorted_arr = list()

    for i in arr:
        count[i] += 1
    
    for i in range(max_arr+1):
        for _ in range(count[i]):
            sorted_arr.append(i)
    return sorted_arr
import sys
n = int(sys.stdin.readline().rstrip())
arr = list()
for i in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))
for i in counting_sort(arr):
    print(i)