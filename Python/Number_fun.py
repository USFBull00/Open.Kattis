questions = int(input())
q_numbers = 1
while q_numbers <= questions:
    n1, n2, n3 = input().split()
    n1, n2, n3 = int(n1),int(n2),int(n3)
    if n1 + n2 == n3:
        print('Possible')
        q_numbers = q_numbers + 1
    elif n1 - n2 == n3:
        print("Possible")
        q_numbers = q_numbers + 1
    elif n2 - n1 == n3:
        print("Possible")
        q_numbers = q_numbers + 1
    elif n1 * n2 == n3:
        print("Possible")
        q_numbers = q_numbers + 1
    elif n2 * n1 == n3:
        print("Possible")
        q_numbers = q_numbers + 1
    elif n1/n2 == n3:
        print("Possible")
        q_numbers = q_numbers + 1
    elif n2/n1 == n3:
        print("Possible")
        q_numbers = q_numbers + 1
    else:
        print("Impossible")
        q_numbers = q_numbers + 1