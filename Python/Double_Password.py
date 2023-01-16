word1 = input()
word2 = input()

combo = 1

for i in range(4):
    if word1[i] != word2[i]:
        combo *= 2

print(combo)