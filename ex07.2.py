# Weighted average: note 1 has weight 3, note 2 has weight 2, and note 3 has weight 1
note1 = float(input('Enter the first grade: '))
note2 = float(input('Enter the second grade: '))
note3 = float(input('Enter the third grade: '))
weighted_average = (note1 * 3 + note2 * 2 + note3) / 5
print('The weighted average of the grades is: {}'.format(weighted_average))
