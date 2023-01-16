#Electrical Outlets, difficulty 1.3
x = int(input())

for i in range(x):
    outlets = input().split()
    total = 0
    for j in outlets[1:]:
        j = int(j)
        total += j
    plugs = len(outlets)
    output = total - plugs +2
    print(output)
    total = 0