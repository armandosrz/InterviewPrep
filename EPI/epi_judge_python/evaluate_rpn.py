from test_framework import generic_test


def evaluate(expression):
    stack = []
    operator = {
        '+': lambda y,x: x+y,
        '-': lambda y,x: x-y,
        '*': lambda y,x: x*y,
        '/': lambda y,x: int(x/y),
    }

    for x in expression.split(','):
        if x in operator:
            stack.append(operator[x](stack.pop(), stack.pop()))
        else:
            stack.append(int(x))

    return stack.pop()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("evaluate_rpn.py", 'evaluate_rpn.tsv',
                                       evaluate))
