#triangulos
seg1 = float(input('Enter the length of the first segment: '))
seg2 = float(input('Enter the length of the second segment: '))
seg3 = float(input('Enter the length of the third segment: '))

if seg1 == seg2 == seg3:
    print('The segments can form an EQUILATERAL triangle.')
elif seg1 == seg2 or seg1 == seg3 or seg2 == seg3:
    print('The segments can form an ISOSCELES triangle.')
else:
    print('The segments can form a SCALENE triangle.')
