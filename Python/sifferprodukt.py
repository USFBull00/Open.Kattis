n = input()
R = 0
while R == 0:
    for i in n:
        if int(i) == 0:
            continue
        if R == 0:
            R = int(i)
        else:
            R = R *int(i)
    if R < 10:
        break
    n = str(R)
    R = 0
print(R)