N = input()
N = int(N)
numbers = input().split(' ')

total = 0
for i in numbers:
    total += int(i)
print(total)