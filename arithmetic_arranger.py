def arithmetic_arranger(problems, answers = False):
    
    # error too many problems
    if len(problems) > 5:
        raise Exception("Error: Too many problems.")

    op1s = []
    operators = []
    op2s = []
    lines = []
    results = []

    for problem in problems:
        # split into parts
        [op1, operator, op2] = problem.split()

        # error for -/+
        if operator not in {"-", "+"}:
            raise Exception("Error: Operator must be '+' or '-'.")

        # error for problem > 4 digits
        if len(op1) > 4 or len(op2) > 4:
            raise Exception("Error: Numbers cannot be more than four digits.")

        # error digits only
        try:
            int(op1)
            int(op2)
        except ValueError:
            raise Exception("Error: Numbers must only contain digits.")

        # parts
        op1s.append(op1)
        operators.append(operator)
        op2s.append(op2)
        lines.append((max(len(op1),len(op2))+2)*'-')
        results.append(eval(problem))

    # results
    i = 0

    line1 = ''
    line2 = ''
    line3 = ''
    line4 = ''
    
    for i in range(len(problems)):
        # line1
        if i != 0:
          line1 += 4 * ' '
        line1 += (len(lines[i]) - len(op1s[i])) * ' ' + str(op1s[i])


        # line2
        if i != 0:
          line2 += 4 * ' '
        line2 += str(operator[i]) + (len(lines[i])-1 - len(op2s[i]))*' ' + str(op2s[i])    

        # line3
        if i != 0:
          line3 += 4 * ' '
        line3 += lines[i]

        # line4
        if i != 0:
          line4 += 4 * ' '
        line4 += (len(lines[i])-1 - len(str(results[i])))*' ' + str(results[i])

        print(line1, line2, line3, line4)

    arranged_outcome = line1 + '\n' + line2 + '\n' + line3
    if answers == True:
      arranged_outcome += '\n' + line4
        
    return arranged_outcome
