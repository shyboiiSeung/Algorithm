A = int(input())
B = int(input())
C = int(input())
D = A+B+C
if A==60 and B==60 and C==60:
    print("Equilateral")
elif D==180 and (A==B or B==C or A==C):
    print("Isosceles")
elif D==180 and A!=B and B!=C and A!=C:
    print("Scalene")
else:
    print("Error")