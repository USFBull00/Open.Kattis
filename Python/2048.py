#2048, difficulty 2.8, in progress

line1 = input().split()
line2 = input().split()
line3 = input().split()
line4 = input().split()
move = input()

if move == '0':
    for i in [line1, line2, line3, line4]:
        if i[1] == i[2]:
            i[1] = int(i[1])*2
            i[2] = i[3]
            i[4] = '0'
        elif i[2] == i[3]:
            i[2] = int(i[2])*2
            i[3] = i[4]
            i[4] = '0'
        elif i[3] == i[4]:
            i[3] = int(i[3]*2)
            i[4] = '0'

print(line1)
print(line2)
print(line3)
print(line4)