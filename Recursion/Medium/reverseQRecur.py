class queue:
    def __init__(self):
        self.queue = []
        pass

    def __repr__(self):
        return str(self.queue)

    def put(self, value):
        self.queue.append(value)
        return value

    def empty(self):
        if len(self.queue) == 0:
            return True
        return False

    def push(self, value):
        self.queue.append(value)
        return value

    def get(self):
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def front(self):
        return self.queue[0]


def reverse(Qew: queue):
    # Base Case being an empty queue
    if Qew.empty():
        return Qew

    # Essentially de-queue and enqueue the items in the list
    else:
        item = Qew.get()
        Qew = reverse(Qew)
        Qew.put(item)
        return Qew


Qew1 = queue()

Qew1.put(1)
Qew1.put(2)
Qew1.put(3)
Qew1.put(4)
Qew1.put(5)
Qew1.put(6)

print(Qew1)
print(reverse(Qew1))
