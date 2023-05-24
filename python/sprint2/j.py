class Node:
    def __init__(self, value=None, next_item=None):
        self.value = value
        self.next_item = next_item


class ListQueue:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.lenght = 0

    def put(self, num):
        if self.lenght == 0:
            self.head = Node(value=num)
            self.tail = self.head
            self.lenght += 1
        else:
            self.tail.next_item = Node(value=num)
            self.tail = self.tail.next_item
            self.lenght += 1

    def size(self):
        return self.lenght

    def get(self):
        if self.lenght == 0:
            return 'error'
        elif self.lenght == 1:
            x = self.head.value
            self.head.value = None
            self.lenght -= 1
            return x
        else:
            x = self.head.value
            self.head = self.head.next_item
            self.lenght -= 1
            return x


q = ListQueue()
i = int(input())
while i:
    i -= 1
    com = input()
    com = com.split()
    if com[0] == 'put':
        q.put(int(com[1]))
    elif com[0] == 'get':
        print(q.get())
    elif com[0] == 'size':
        print(q.size())
