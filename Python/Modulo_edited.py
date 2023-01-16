#Modulo, difficulty 1.7
count = 0
l1 = []
for _ in range(10):
    i = int(input())
    #for i in map(int, input()):
    #    j = map(int, input())
    x = (i % 42)
    if x not in l1:
        count += 1
        l1.append(x)
print(count)