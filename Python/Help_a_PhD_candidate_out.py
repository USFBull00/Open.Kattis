#Help a PhD candidate out!, difficulty 1.7

total = int(input())
for i in range(total):
    y = input()
    if y == 'P=NP':
        print('skipped')
    else:
        position = int(y.find('+'))
        a = y[0:position]
        b = y[(position+1):]
        sum = int(a) + int(b)
        print(sum)