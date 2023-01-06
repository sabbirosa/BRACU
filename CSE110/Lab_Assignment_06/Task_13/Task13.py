operator = input()
operand1 = int(input())
operand2 = int(input())

def basic_cal(operator, first_operand, second_operand):
    if operator == "+":
        return first_operand + second_operand
    elif operator == "-":
        result = first_operand - second_operand
    elif operator == "*":
        result = first_operand * second_operand
    elif operator == "/":
        result = first_operand / second_operand
    else:
        result = "Invalid operator"
    return result

print(basic_cal(operator, operand1, operand2))