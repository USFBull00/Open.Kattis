#Missing Numbers, difficulty 1.7
inp = []
number = input()
for i in range(int(number)):
    a = input()
    inp.append(int(a))
maxim = max(inp)
total = []
for i in range(1, maxim):
    total.append(i)
count = 0
for i in total:
    if i not in inp:
        print(i)
        count += 1
if count == 0:
    print('good job')

