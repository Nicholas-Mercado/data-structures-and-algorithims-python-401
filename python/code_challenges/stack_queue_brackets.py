from data_structures.stack import Stack


def multi_bracket_validation(string):

    stack = Stack()

    for char in string:
        if char == '[':
            stack.push(']')

        if char == ']':
            if stack.top:
                if stack.top.value == char:
                    stack.pop()
                else:
                    return False
            
    return True




