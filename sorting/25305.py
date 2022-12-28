n,k = map(int, input().split())
li = list(map(int, input().split()))
print(sorted(li, reverse=True)[k-1])