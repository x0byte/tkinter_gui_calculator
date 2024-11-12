def add_digit(current_text, digit):
    #adding a digit to the current input
    return current_text + str(digit)

def set_operator(current_text, op):

    first_operand = float(current_text) if current_text else 0
    return first_operand, op

def calculate_results(first_operand, operator, second_operand):

    result = 0

    if operator == "+":
        result = first_operand + second_operand
    elif operator == "-":
        result = first_operand - second_operand
    elif operator == "*":
        result = first_operand * second_operand
    elif operator == "/" and second_operand != 0:
        result = first_operand / second_operand
    else:
        return "Error"
    
    return result

def clear_display():
    return ""