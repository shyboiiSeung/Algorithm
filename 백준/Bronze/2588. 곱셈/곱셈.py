A = int(input())
B = int(input())
print(A*(B%10)) #5
print(A*(int(B/10)%10)) #8
print(A*int(B/100)) #3
print(A*B)