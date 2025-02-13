##Aprimore o desafio anterior, mostrando no final: 
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.
sum_even = 0  
sum_third_column = 0  
max_second_row = float('-inf')  
matrix = []  

for i in range(3):
    row = []  
    for j in range(3):
        n = int(input(f"Enter the number for position ({i+1}, {j+1}): "))
        
        if n % 2 == 0:
            sum_even += n
        
        if j == 2:
            sum_third_column += n
        
        if i == 1 and n > max_second_row:
            max_second_row = n
        
        row.append(n)
    matrix.append(row)

print("\n3x3 Matrix:")
for row in matrix:
    print(" ".join([str(num) for num in row]))

print(f"\nA) Sum of all even values: {sum_even}")
print(f"B) Sum of values in the third column: {sum_third_column}")
print(f"C) Highest value in the second row: {max_second_row}")
