import Node
class LinkedList():
    def __init__(self):
        self.head = None

    def __init__(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            searcher = self.head
            while searcher.next != None:
                searcher = searcher.next
            searcher.next = new_node

    def __contains__(self, target):
        traverser = self.head
        while traverser != None:
            if traverser.data == target:
                return True
            traverser = traverser.next
        return False

