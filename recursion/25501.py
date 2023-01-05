import sys

def recursion(s, l, r, n):
    if l >= r: return 1,n+1
    elif s[l] != s[r]: return 0,n+1
    else: 
        n += 1
        return recursion(s, l+1, r-1, n)

def isPalindrome(s):
    n = 0
    return recursion(s, 0, len(s)-1, n)

N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    text = sys.stdin.readline().rstrip()
    ret, cnt = isPalindrome(text)
    print(ret, cnt)