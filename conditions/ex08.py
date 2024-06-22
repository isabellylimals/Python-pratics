#segmentos de um triangulo

seg1 = float(input("\033[37mEnter the length of the first segment: "))
seg2 = float(input("\033[37mEnter the length of the second segment: "))
seg3 = float(input("\033[37mEnter the length of the third segment: "))

if seg1 + seg2 > seg3 and seg1 + seg3 > seg2 and seg2 + seg3 > seg1:
    print('\033[1;32mThese segments can form a triangle.\033[0m')
else:
    print('\033[1;31;40mThese segments cannot form a triangle.\033[0m')
