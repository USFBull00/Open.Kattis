highest_score = 0
for i in range(1,6):
    a, b, c, d = input().split()
    score = int(a)+int(b)+int(c)+int(d)
    if score > highest_score:
        highest_score = score
        winner = i
print(winner, highest_score)
