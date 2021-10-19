def arithmetic_arranger(problems, answers=False):

    if len(problems) > 5:
        return "Error: Too many problems."

    formatter = ["", "", "", ""]

    for problem in problems:
        # split into parts
        [op1, operator, op2] = problem.split()

        if operator not in {"-", "+"}:
            return "Error: Operator must be '+' or '-'."

        if len(op1) > 4 or len(op2) > 4:
            return "Error: Numbers cannot be more than four digits."

        try:
            int(op1), int(op2)
        except ValueError:
            return "Error: Numbers must only contain digits."

        # form rows
        lines = (max(len(op1), len(op2)) + 2) * "-"
        result = str(eval(problem))

        for i in range(4):
            if formatter[i] != "":
                formatter[i] += 4 * " "
        formatter[0] += (len(lines) - len(op1)) * " " + op1
        formatter[1] += operator + (len(lines) - 1 - len(op2)) * " " + op2
        formatter[2] += lines
        formatter[3] += (len(lines) - len(result)) * " " + result

    output = ""
    for i in range(4):
        if answers == False and i == 3:
            break
        if output != "":
            output += "\n"
        output += formatter[i]

    return output
