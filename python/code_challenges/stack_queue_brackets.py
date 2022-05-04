# from data_structures.queue import Queue
from data_structures.stack import Stack


def multi_bracket_validation(value):

    stack = []

    for data in value:

        if data == '(' or data == '[' or data == '{':
            stack.append(data)
        else:

            if not stack:
                return False
            else:

                top = stack[-1]
                if data == ')' and top == '(' or \
                        data == ']' and top == '[' or \
                        data == '}' and top == '{':
                    stack.pop()

    if not stack:
       return True
    else:
        return False


