N,M = map(int,input().split())
arr = list()
for i in range(N):
    arr.append(input())
        
ans = 123456789
for i in range(N-7):
    for j in range(M-7):
        # print(i,j)
        cnt = 0
        for x in range(8):
            for y in range(8):
                if ((x+y)%2==0)&(arr[i+y][j+x]!='B'):
                    cnt += 1
                elif ((x+y)%2==1)&(arr[i+y][j+x]!='W'):
                    cnt += 1
        if cnt > 32:
            cnt = 64-cnt
        if cnt < ans:
            ans = cnt
print(ans)