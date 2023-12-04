class stack:
    def __init__(self):
        self.item = []

    def empty(self):
        return self.item == []

    def push(self, number):
        self.item.insert(0, number)

    def pop(self):
        return self.item.pop(0)

    def print_stack(self):
        print(self.item)


number = stack()
number.push(5)
number.print_stack()