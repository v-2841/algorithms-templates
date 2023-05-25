# 87694411
from operator import add, sub, mul, floordiv


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self, pos=-1):
        try:
            return self.items.pop(pos)
        except IndexError:
            raise IndexError('List is empty.')


def polish_calculator(expression):
    operations = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': floordiv,
    }
    stack = Stack()
    for i in expression:
        if i in operations:
            stack.push(operations[i](stack.pop(-2), stack.pop()))
        else:
            stack.push(int(i))
    return stack.pop()


if __name__ == '__main__':
    expression = input().split()
    print(polish_calculator(expression))
