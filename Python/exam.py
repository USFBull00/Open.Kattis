#Exam, difficulty 1.8
matching = 0
friends_score = int(input())
my_answer = input()
friends_answer = input() 
total_questions = int(len(my_answer))
#print(total_questions)
#print(my_answer)
for i in range(total_questions):
  #print(my_answer[i])
  if my_answer[i] == friends_answer[i]:
    matching += 1
#print(matching)
max_score = total_questions - abs(matching - friends_score)
print(max_score)