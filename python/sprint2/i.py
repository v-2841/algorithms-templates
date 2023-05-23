class MyQueueSized:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.lenght = 0

    def is_empty(self):
        return self.lenght == 0

    def push(self, x):
        if self.lenght != self.max_size:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_size
            self.lenght += 1
        else:
            print('error')

    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.lenght -= 1
        return x

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.head]

    def size(self):
        return self.lenght


i = int(input())
mas = MyQueueSized(int(input()))
while i:
    i -= 1
    com = input()
    com = com.split()
    if com[0] == 'push':
        mas.push(int(com[1]))
    elif com[0] == 'pop':
        print(mas.pop())
    elif com[0] == 'peek':
        print(mas.peek())
    elif com[0] == 'size':
        print(mas.size())
