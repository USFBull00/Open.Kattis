#Espresso!, difficulty 2.1
n, s = input().split()
students = int(n)
size = int(s)

refills = 0
left_over = size

for i in range(students):
    order = input()
    shots = int(order[0])
    needed = 0
    needed += shots
    if order[-1] =='L':
        needed += 1
    if left_over >= needed:
        left_over -= needed
    elif left_over < needed:
        refills += 1
        left_over = size - needed
    #print(order, needed, left_over, refills)

print(refills)