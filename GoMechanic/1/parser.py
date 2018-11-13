import json
import numbers


def if_else_parser(statement):
    expr = statement["if"]
    flag = evaluate(expr)
    true_value = statement["then"]
    false_value = statement["else"]

    if flag:
        return_value = true_value
    else:
        return_value = false_value

    if isinstance(return_value, str):
        return_value = get_value_from_input(return_value, True)
        return return_value
    elif isinstance(return_value, numbers.Number):
        return return_value
    elif isinstance(return_value, dict):
        return if_else_parser(return_value)


def evaluate(expr):
    left = expr['left']
    right = expr['right']
    op = expr['op']
    left = get_value_from_input(left, False)
    right = get_value_from_input(right, False)

    if op == "==":
        if left == right:
            return True

    elif op == ">":
        if left > right:
            return True

    elif op == "<":
        if left < right:
            return True

    else:
        raise Exception("invalid input format")
    return False


def get_value_from_input(value, flag):
    if value not in inp and flag:
        return value
    if isinstance(value, str):
        value = inp[value]
    elif isinstance(value, numbers.Number):
        pass
    else:
        raise Exception("invalid input format")
    return value


# loading expression
with open("expression.json") as f:
    data = json.load(f)

# loading input file
with open("input.json") as f:
    inp = json.load(f)

if isinstance(data, dict):
    print(if_else_parser(data))
else:
    raise Exception("invalid input format")
