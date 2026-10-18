location = 'A'
A = 'Dirty'
B = 'Dirty'

while A == 'Dirty' or B == 'Dirty':
    if location == 'A':
        if A == 'Dirty':
            print("Suck dirt in Room A")
            A = 'Clean'
        else:
            print("Move to Room B")
            location = 'B'
    elif location == 'B':
        if B == 'Dirty':
            print("Suck dirt in Room B")
            B = 'Clean'
        else:
            print("Move to Room A")
            location = 'A'

print("Both rooms are clean")
