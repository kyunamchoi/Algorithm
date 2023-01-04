import sys

n = int(sys.stdin.readline().rstrip())

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)
print(factorial(n))