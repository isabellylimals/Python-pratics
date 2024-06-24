#media
grade1 = float(input('Enter the first grade: '))
grade2 = float(input('Enter the second grade: '))
grade3 = float(input('Enter the third grade: '))
average = (grade1 + grade2 + grade3) / 3

if average < 5.0:
    print('YOU FAILED :(, your average was: {:.2f}'.format(average))
elif 5.0 <= average < 6.9:
    print('YOU ARE IN RECOVERY, your average was: {:.2f}'.format(average))
elif average >= 7.0:
    print('CONGRATULATIONS, YOU PASSED, your average was: {:.2f}'.format(average))
else:
    print('Invalid input. Please enter valid grades.')
