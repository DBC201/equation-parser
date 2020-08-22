class Stack:
    def __init__(self, inp=None):
        self.data = []
        if inp:
            self.push(*inp)

    def push(self, data):
        self.data.append(data)

    def pop(self):
        if self.isEmpty():
            raise IndexError("pop from empty stack")
        return self.data.pop(len(self.data) - 1)

    def peek(self):
        if self.isEmpty():
            raise IndexError("peek from empty stack")
        return self.data[len(self.data) - 1]

    def isEmpty(self):
        if len(self.data) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.data)

    def __str__(self):
        return str(self.data)
