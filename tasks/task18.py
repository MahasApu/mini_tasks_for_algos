from typing import List

expressions = []
with open(r"C:\Users\vaskm\PycharmProjects\tasks_for_algos\tasks\input_task18.txt", "r") as file:
    for line in file.readlines():
        expressions.append(line.split())


def ret_priority(operator: str) -> int:
    operator_priority = {
        "(": -1,
        ")": 0,
        "^": 1,
        "*": 2, "/": 2, "%": 2,
        "+": 3, "-": 3,
        "<<": 4, ">>": 4,
        "<": 5, "<=": 5, ">": 5, ">=": 5,
        "&": 6,
        "|": 7,
        "&&": 8,
        "||": 9,
    }
    return operator_priority[operator]


def to_RPN(expression: List[str]) -> List[str]:
    right_assoc_operators = ["^"]
    all_operators = ["^", "*", "/", "%", "+", "-", "<<", ">>", "<", "<=", ">", ">=", "&", "|", "&&", "||", ")", "("]
    stack = []
    result = []
    for elem in expression:
        if elem in all_operators:
            if elem == "(":
                stack.append(elem)
            else:
                while stack and (
                        ret_priority(stack[-1]) >= ret_priority(elem)
                        and elem not in right_assoc_operators
                ):
                    result.append(stack.pop())
                if elem == ')':
                    stack.pop()
                else:
                    stack.append(elem)
        else:
            result.append(elem)

    while stack:
        result.append(stack.pop())
    return result


def to_calc(expression: List[str]) -> int:
    operators = {"^": (lambda x, y: x ** y), "*": (lambda x, y: x * y), "/": (lambda x, y: x // y),
                 "%": (lambda x, y: x % y), "+": (lambda x, y: x + y), "-": (lambda x, y: x - y),
                 "<<": (lambda x, y: x << y), ">>": (lambda x, y: x << y), "<": (lambda x, y: x < y),
                 "<=": (lambda x, y: x <= y), ">": (lambda x, y: x > y), ">=": (lambda x, y: x >= y),
                 "&": (lambda x, y: x & y), "|": (lambda x, y: x | y), "&&": (lambda x, y: x and y),
                 "||": (lambda x, y: x or y)}
    polish = to_RPN(expression)
    stack = []
    for elem in polish:
        if elem in operators:
            elem2, elem1 = stack.pop(), stack.pop()
            result = operators[elem](elem1, elem2)
        else:
            result = int(elem)
        stack.append(result)

    return stack.pop()
