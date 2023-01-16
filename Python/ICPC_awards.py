#ICPC awards, difficulty 1.5
total = int(input())
ulist = []
winners = 1
for i in range(total):
    university, team = input().split()
    if university not in ulist:
        if winners <= 12:
            print(university, team)
        winners += 1
        ulist.append(university)
