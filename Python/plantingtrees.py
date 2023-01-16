#Planting Trees, difficulty 1.7
num = int(input())
trees = input().split()
for i in range(0, len(trees)):
    trees[i] = int(trees[i])
trees.sort(reverse=True)
minday = 0
for i in range(num): 
    if (minday < int(trees[i])+i+1):
      minday = int(trees[i])+i+1

print(minday+1)