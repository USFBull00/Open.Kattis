#99 Problems, difficulty 2.7
price_str = input()
price = int(price_str)

first = price_str[:-2]
#print(first)

upper_str = first + '99'
upper = int(upper_str)

if first != '':
    lower_prep = int(first) - 1
    lower_str = str(lower_prep) + '99'
else:
    lower_str = '99'

lower = int(lower_str)

if abs(price - upper)>abs(price - lower):
    print(lower)
if abs(price - lower)>=abs(price - upper):
   print(upper)
