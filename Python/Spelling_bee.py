#Spelling Bee, difficulty 2.1
test_case = input()
number_of_words = int(input())

for i in range(number_of_words):
    i = input()
    if len(i)>3:
        if test_case[0] in i:
            sum = 0
            for l in range(len(i)):
                if i[l] in test_case:
                    sum += 1
                else: continue
            if sum == len(i):
                print(i)

