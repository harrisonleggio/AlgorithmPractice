# Node class
class Node:

    # instantiate node with data and next node to nothing
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList class
class LinkedList:

    # instantiate head and tail to nothing
    def __init__(self):
        self.head = None
        self.tail = None

    # adds new node
    def addNode(self, data):
        new_node = Node(data)           # creates new node

        if self.head == None:           # if list is empty, sets new node to head
            self.head = new_node

        if self.tail != None:           # if list has head and tail, adds new node to end
            self.tail.next = new_node

        self.tail = new_node            # if list has length 1, sets new node to tail

    # removes node at given index
    def removeNode(self, data):
        prev = None
        node = self.head

        while node is not None:
            if (node.data == data):
                if (prev is not None):
                    prev.next = node.next
                else:
                    self.head = node.next

            prev = node
            node = node.next

    # prints Linked List
    def printList(self):
        node = self.head                # temporary placeholder for head
        while node != None:             # traverses entire Linked List
            print (node.data)           # prints node's data
            node = node.next            # moves to next node

    # prints size of Linked List
    def size(self):
        node = self.head                # temporary placeholder for head
        counter = 0                     # counter
        while node != None:             # traverses entire Linked List
            counter += 1                # increments counter
            node = node.next            # moves to next node
        return counter                  # returns counter, which is the size of the Linked List

def main():
    List = LinkedList()
    List.addNode(10)
    List.addNode(20)
    List.addNode(30)
    List.addNode(40)
    List.printList()
    List.removeNode(20)
    List.printList()