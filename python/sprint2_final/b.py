# 87783450
from operator import add, sub, mul, floordiv


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        try:
            return self.items.pop()
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
            first_num, second_num = stack.pop(), stack.pop()
            stack.push(operations[i](second_num, first_num))
        else:
            stack.push(int(i))
    return stack.pop()


if __name__ == '__main__':
    expression = input().split()
    print(polish_calculator(expression))
