#Quality-Adjusted Life-Year, difficulty 1.3
total = 0
N = int(input())
for i in range(N):
    q, y = input().split()
    total += float(q)*float(y)
print(format(total, '.3f'))
