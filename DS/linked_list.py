class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self,values):
        self.head = None

        if values is not None:

            node = Node(values.pop(0))

            self.head = node

            for value in values:
                node.next = Node(value)
                node = node.next

    def __repr__(self):

        node = self.head
        nodes = []

        while node:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return '->'.join(nodes)
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def add_first(self,value):
        node = Node(value)
        if self.head is not None:
            node.next = self.head
            self.head = node
        else:
            self.head = node
    def add_last(self, value):
        node = Node(value)

        
            

linkedList = LinkedList(['1','2','3'])
linkedList.add_first('c')
print(linkedList)
