# 87656065
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


if __name__ == '__main__':
    expression = input().split()
    stack = Stack()
    for i in expression:
        if i == '+':
            x = stack.pop()
            y = stack.pop()
            stack.push(x+y)
        elif i == '-':
            x = stack.pop()
            y = stack.pop()
            stack.push(y-x)
        elif i == '*':
            x = stack.pop()
            y = stack.pop()
            stack.push(x*y)
        elif i == '/':
            x = stack.pop()
            y = stack.pop()
            stack.push(y//x)
        else:
            stack.push(int(i))
    print(stack.pop())
