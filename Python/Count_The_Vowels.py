#Count the vowels, difficulty 1.4
string = input()
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

top = len(string)
result = 0

for i in range(top):
    if string[i] in vowels:
        result += 1

print(result)