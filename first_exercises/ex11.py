# Painting a wall
height = float(input('Enter the height of the wall: '))
width = float(input('Enter the width of the wall: '))
wall_area = height * width
paint_liters = wall_area / 2
print('The area of the wall is: {:.2f}m^2 and you will need {:.2f} liters of paint.'.format(wall_area, paint_liters))
