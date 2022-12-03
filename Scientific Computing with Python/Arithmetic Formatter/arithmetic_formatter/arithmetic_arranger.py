def arithmetic_arranger(problems, *args):
    if len(problems) > 5:
        return "Error: Too many problems."
    else:
        calcs = []
        results = []
        for problem in problems:
            num = []
            for element in problem.split():
                num.append(element)
            if "*" in num or "/" in num:
                return "Error: Operator must be '+' or '-'."
            elif num[0].isdigit() is False or num[2].isdigit() is False:
                return "Error: Numbers must only contain digits."
            elif len(num[0]) > 4 or len(num[2]) > 4:
                return "Error: Numbers cannot be more than four digits."
            else:
                num[0] = int(num[0])
                num[2] = int(num[2])
            calcs.append(num)

        for operation in calcs:
            if operation[1] == "+":
                op = operation[0] + operation[2]
            else:
                op = operation[0] - operation[2]
            results.append(op)

        op1 = []
        op2 = []
        dash_lines = []
        res = []

        for i in range(len(calcs)):
            if calcs[i][0] < calcs[i][2]:
                dash_length = len(str(calcs[i][2]))
            else:
                dash_length = len(str(calcs[i][0]))

            dashes = "-" * dash_length
            position1 = f"  {calcs[i][0]: >{dash_length}}"
            position2 = f"{calcs[i][1]} {calcs[i][2]: >{dash_length}}"
            position3 = dashes.rjust(dash_length + 2, "-")
            position4 = f" {results[i]: >{dash_length + 1}}"

            op1.append(position1)
            op2.append(position2)
            dash_lines.append(position3)
            res.append(position4)

        s = " " * 4
        j = "\n"
        if True in args:
            arranged_problems = s.join(op1) + j + s.join(op2) + j + s.join(dash_lines) + j + s.join(res)
        else:
            arranged_problems = s.join(op1) + j + s.join(op2) + j + s.join(dash_lines)
        return arranged_problems
