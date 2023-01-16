#Simon Says, difficulty 1.7
x = input()
Simon = 'Simon says'
for i in range(int(x)):
    i = input()
    if Simon in i:
        outp = i[11:]
        print(outp)