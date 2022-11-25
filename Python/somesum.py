n = input()
n = int(n)
if (n % 2) == 1:
  print('Either')
else:
  if ((n/2) % 2) == 0:
    print('Even')
  else:
    print('Odd')
