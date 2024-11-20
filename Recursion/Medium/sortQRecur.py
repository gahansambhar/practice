class queue:
    def __init__(self):
        self.queue = []
        pass

    def __repr__(self):
        return self.queue

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
