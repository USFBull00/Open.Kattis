#Bela, difficulty 1.4

#hand = input()[1]
#for i in input()
 #   if i[1] == hand then if i[0] == A then total = total +11
 #                       if i[0] == K then total = total +4
  #                      if i[0] == Q then total = total +3
   #                     if i[0] == J then total = total +20
    #                    if i[0] == T then total = total +10
     #                   if i[0] == 9 then total = total +14
    #if i[1] =/= hand then if i[0] == A then total = total +11
 #                       if i[0] == K then total = total +4
 #                       if i[0] == Q then total = total +3
 #                       if i[0] == J then total = total +2
   #                     if i[0] == T then total = total +10
#print(total)
first_line = input().split(' ')
total_hands = int(first_line[0])
dominant_suit = first_line[1]
i = 0
max_i = total_hands * 4
total_points = 0

def compute_hand_score(card, suit, dominant_suit):
    if suit == dominant_suit:
        return dominant_values[card]
    return values[card]

values = {
    'A': 11,
    'K': 4,
    'Q': 3,
    'J': 2,
    'T': 10,
    '9': 0,
    '8': 0,
    '7': 0
}

dominant_values = {
    'A': 11,
    'K': 4,
    'Q': 3,
    'J': 20,
    'T': 10,
    '9': 14,
    '8': 0,
    '7': 0
}

while i < max_i:
    line = input()
    total_points += compute_hand_score(line[0], line[1], dominant_suit)
    i += 1

print(total_points)

