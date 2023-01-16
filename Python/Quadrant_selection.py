#Quadrant Selection, difficulty 1.3
number1 = int(input())
for i in range(1):
    number2 = int(input())
if number1>0 and number2>0 :
    print(1)
if number1<0 and number2>0:
    print(2)
if number1<0 and number2<0:
    print(3)
if number1>0 and number2<0:
    print(4)