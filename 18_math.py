def clean_eval(expression):  # NO PARENTHESES!!!
    print(f"evaluating {expression}")
    if expression == []:
        return 0
    if len(expression) == 1:
        return int(expression[0])
    else:
        first_operand = int(expression[0])
        operator = expression[1]
        second_operand = int(expression[2])

        if operator == '+':
            return clean_eval([first_operand + second_operand] + expression[3:])
        else:
            return first_operand * clean_eval(expression[2:])




def x_eval(expression):
    # the statement in stack[i] is at depth i
    stack = [] 
    this_statement = []

    #build this_statement until you hit a paren
    for item in expression: 
        # print(item)
        # print(stack)
        # push statement to stack and start a new one
        if item.startswith('('):
            for x in range(item.count('(')):
                stack.append(this_statement)
                this_statement = []
            this_statement.append(item.lstrip('('))

        elif item.endswith(')'):
            this_statement.append(item.rstrip(')'))
            for x in range(item.count(')')):
                eval_statement = clean_eval(this_statement)
                this_statement = stack.pop()
                this_statement.append(eval_statement)
                print(f"closing paren: {this_statement}")
        else:
            this_statement.append(item)
    
    return clean_eval(this_statement)
    



lines = [line.strip().split() for line in open("input", "r").readlines()]
total = 0
for line in lines:
    print(line)
    print(x_eval(line))
    total += x_eval(line)
print(total)
