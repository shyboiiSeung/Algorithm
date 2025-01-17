num = int(input())
numbers = list(map(int,input().split()))
find = int(input())

count = 0

for i in range(num):
    if numbers[i] == find:
        count = count + 1

print(count)