class StackMax:
    def __init__(self):
        self.items = []

    def push(self, item):
        if self.items:
            if self.items[-1][1] < item:
                self.items.append((item, item))
            else:
                self.items.append((item, self.items[-1][1]))
        else:
            self.items.append((item, item))

    def pop(self):
        if not self.items:
            print('error')
        else:
            self.items.pop()

    def get_max(self):
        if not self.items:
            print('None')
        else:
            print(self.items[-1][1])


i = int(input())
stack = StackMax()
while i:
    i -= 1
    com = input()
    com = com.split()
    if com[0] == 'push':
        stack.push(int(com[1]))
    elif com[0] == 'pop':
        stack.pop()
    elif com[0] == 'get_max':
        stack.get_max()
