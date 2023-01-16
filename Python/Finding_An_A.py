#Finding An A, difficulty 1.3
string = input()
top = len(string)
#print(top)

#print(string[top])
for i in range(0,top):
    #print(string[i])
    if string[i] == 'a':
        print(string[i:top])
        break
