#Pot, difficulty 1.4
total = 0
N = int(input())
for i in range(N):
    y = input()
    number = y[:-1]
    power = y[-1]
    raised = int(number)**int(power)
    total = total + raised
print(total)