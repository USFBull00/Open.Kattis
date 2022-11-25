R, C, ZR, ZC = input().split()
R = int(R); C = int(C); ZR = int(ZR); ZC = int(ZC)
for i in range(R):
  _output = ''
  line = input()
  for j in range(C):
    character = line[j]
    _output += ZC*character
  for k in range(ZR):
    print(_output)