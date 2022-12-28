def counting_sort(arr):
    max_arr = max(arr)
    count = [0] * (max_arr+1)
    sorted_arr = list()

    for i in arr:
        count[i] += 1
    
    for i in range(max_arr+1):
        for _ in range(count[i]):
            sorted_arr.append(i)
    return sorted_arr

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

sorted_arr = counting_sort(arr)

for i in sorted_arr:
    print(i)