# 87783554
class Dequeue:
    def __init__(self, max_n):
        self.nums = [None] * max_n
        self.max_n = max_n
        self.head = 0
        self.tail = 0
        self.lenght = 0

    def push_front(self, new_num):
        if self.lenght != self.max_n:
            self.nums[self.head - 1] = new_num
            self.head = (self.head - 1) % self.max_n
            self.lenght += 1
        else:
            raise IndexError('Deque is full.')

    def push_back(self, new_num):
        if self.lenght != self.max_n:
            self.nums[self.tail] = new_num
            self.tail = (self.tail + 1) % self.max_n
            self.lenght += 1
        else:
            raise IndexError('Deque is full.')

    def pop_front(self):
        if self.is_empty():
            raise IndexError('Deque is empty.')
        num = self.nums[self.head]
        self.nums[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.lenght -= 1
        return num

    def pop_back(self):
        if self.is_empty():
            raise IndexError('Deque is empty.')
        num = self.nums[self.tail - 1]
        self.nums[self.tail - 1] = None
        self.tail = (self.tail - 1) % self.max_n
        self.lenght -= 1
        return num

    def is_empty(self):
        return self.lenght == 0


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    deque = Dequeue(max_n=m)
    for _ in range(n):
        cmnd, *prms = input().split()
        try:
            result = getattr(deque, cmnd)(*prms)
            if result:
                print(result)
        except AttributeError:
            print('No such method exists.')
        except TypeError:
            print('Missing argument.')
        except IndexError:
            print('error')
