student = [i for i in range(1,31)]

for _ in range(28):
    no = int(input())
    student.remove(no)

print(min(student))
print(max(student))