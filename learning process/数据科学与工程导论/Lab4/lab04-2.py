class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def empty(self):
        return self.size() == 0

    def size(self):
        return len(self.items)

    def head(self):
        return self.items[0]

    def tail(self):
        return self.items[-1]

if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    print(q.items)
    q.enqueue(5)
    print(q.items)
    q.enqueue(2)
    print(q.items)
    print(q.head())
    print(q.tail())
    print(q.size())
    q.dequeue()
    print(q.items)
    print(q.head())
    print(q.tail())
    print(q.empty())