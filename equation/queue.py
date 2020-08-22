class Queue:
    def __init__(self, data=None):
        self.data = []
        if data:
            self.enqueue(*data)

    def enqueue(self, data):  # adds from rear
        self.data.append(data)

    def dequeue(self):  # removes from front
        if self.isEmpty():
            raise IndexError("dequeue from empty queue")
        return self.data.pop(0)

    def peek(self):
        if self.isEmpty():
            raise IndexError("peek from empty queue")
        return self.data[0]

    def isEmpty(self):
        if len(self.data) == 0:
            return True
        else:
            return False

    def __str__(self):
        return str(self.data)
