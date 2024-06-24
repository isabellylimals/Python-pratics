#Ultrapassagem de velocidade e multa
speed = int(input("Enter the car's speed in km/h: "))

if speed > 80:
    print('You have exceeded the speed limit and have been fined.')
    exceeded_speed = speed - 80
    fine = exceeded_speed * 7
    print('The fine amount is {}R$.'.format(fine))
else:
    print('You are at the correct speed!')
