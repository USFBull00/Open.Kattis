#Tarifa, difficulty 1.4
X = int(input())
data = 0

for i in range(int(input())):
    data += X - int(input())

print(data+X)