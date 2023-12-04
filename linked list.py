class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked:
    def __init__(self):
        self.head = None

    def show(self):
        node = self.head
        while node != None:
            print(node.data)
            node = node.next