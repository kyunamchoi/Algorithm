import sys
inp = sys.stdin.readline().rstrip()
arr = list()
for i in inp:
    arr.append(int(i))
arr.sort(reverse=True)
str_arr = list()
for i in arr:
    str_arr.append(str(i))
print(int("".join(str_arr)))