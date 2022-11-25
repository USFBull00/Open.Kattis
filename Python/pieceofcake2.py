width, h1, v1 = [int(i) for i in input().split()]
h1 = int(h1); v1 = int(v1); width = int(width)
measure1 = []
measure1.append(h1)
h2 = width - h1
measure1.append(int(h2))

measure2 = []
measure2.append(v1)
v2 = width - v1
measure2.append(int(v2))

x1 = max(measure1)
x2 = max(measure2)

volume = x1*x2*4
print(volume)