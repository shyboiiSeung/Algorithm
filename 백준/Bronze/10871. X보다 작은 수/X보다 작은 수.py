A, B = map(int,input().split())
a = list(map(int,input().split()))

for i in range (A):
    if B > a[i]:
        print(a[i],end=' ')