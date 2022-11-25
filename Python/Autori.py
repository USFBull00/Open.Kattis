#name = input(' ')
#initials=name[0]
#for t
#       if name[t] == '-'
#           initials = intials + name[i+1]
#print(initials)

shortname = list()
for letter in input():
    if letter.isupper() == True:
        shortname.append(letter)
print("".join(shortname))