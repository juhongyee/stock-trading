class Node:

    def __init__(self,data = 'None'):
        self.value = data
        self.next = 'None'

class linkedlist:
    def __init__(self,data):
        self.value = data
        self.head = None

    def Addfirst(self,value):
        temp = Node(value)
        temp.next = self.

a = Node(50)
print(a.value)
print(a.next)
