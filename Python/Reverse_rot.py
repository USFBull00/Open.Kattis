key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
x = 0
while x == 0:
    line = input()
    if line == '0':
        break
    shift, string = line.split()
    string = string[::-1]
    newstring = ''
    for i in string:
        location = key.index(i)
        new_location = location + int(shift)
        if new_location > 27:
            new_location = new_location - 28
        newstring = newstring + key[new_location]
    print(newstring)