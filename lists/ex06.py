expression = input("Enter an expression: ")
stack = []

for symbol in expression:
    if symbol == "(":
        stack.append("(")
    elif symbol == ")":
        if len(stack) > 0:
            stack.pop()
        else:
            stack.append(")")
            break

if len(stack) == 0:
    print("The expression is correctly balanced.")
else:
    print("The expression has unbalanced parentheses.")

