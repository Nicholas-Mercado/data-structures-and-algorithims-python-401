from data_structures.stack import Stack


def multi_bracket_validation(string):

    stack = Stack()

    for char in string:
        if (char == ']' or char == '}' or char == ')') and stack.is_empty():
            return False

        if char == '[':
            stack.push(']')

        if char == '{':
            stack.push('}')

        if char == '(':
            stack.push(')')

        if (char == ']' or char == '}' or char == ')'):

            if stack.top.value == char:
                stack.pop()
            else:
                return False

    return True
