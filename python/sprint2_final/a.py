# 87650025
class Queue:
    def __init__(self, max_n):
        self.queue = [None] * max_n
        self.max_n = max_n
        self.head = 0
        self.tail = 0
        self.lenght = 0

    def push_front(self, x):
        if self.lenght != self.max_n:
            self.queue[self.head-1] = x
            self.head = (self.head - 1) % self.max_n
            self.lenght += 1
        else:
            print('error')

    def push_back(self, x):
        if self.lenght != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.lenght += 1
        else:
            print('error')

    def pop_front(self):
        if self.is_empty():
            return 'error'
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.lenght -= 1
        return x

    def pop_back(self):
        if self.is_empty():
            return 'error'
        x = self.queue[self.tail-1]
        self.queue[self.tail-1] = None
        self.tail = (self.tail - 1) % self.max_n
        self.lenght -= 1
        return x

    def is_empty(self):
        return self.lenght == 0


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    deque = Queue(max_n=m)
    for _ in range(n):
        command = input().split()
        if command[0] == 'push_front':
            deque.push_front(int(command[1]))
        elif command[0] == 'push_back':
            deque.push_back(int(command[1]))
        elif command[0] == 'pop_front':
            print(deque.pop_front())
        elif command[0] == 'pop_back':
            print(deque.pop_back())
