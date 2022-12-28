li = []
for _ in range(5):
    li.append(int(input()))
sum = 0
for i in li:
    sum += i
print(int(sum/5))
print(sorted(li)[2])