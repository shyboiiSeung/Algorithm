import sys

test = int(input())

for _ in range(test):
    A, B = map(int,sys.stdin.readline().split())
    print(A+B)