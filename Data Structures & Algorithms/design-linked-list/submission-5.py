class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        count = 0
        curr = self.head

        while count <= index:
            if curr is None:
                return -1

            if count == index:
                return curr.value
            else:
                curr = curr.next
                count += 1

    def addAtHead(self, val: int) -> None:
        if self.head == None:
            self.head = Node(val)
            self.head.next = None
            self.head.previous = None

            self.tail = self.head
            return
        
        newNode = Node(val)

        newNode.previous = None
        newNode.next = self.head

        self.head.previous = newNode
        self.head = newNode

    def addAtTail(self, val: int) -> None:
        if self.tail == None:
            self.tail = Node(val)
            self.tail.next = None
            self.tail.previous = None

            self.head = self.tail
            return

        newNode = Node(val)

        newNode.previous = self.tail
        newNode.next = None

        self.tail.next = newNode
        self.tail = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        count = 0

        if index == 0:
            self.addAtHead(val)
            return

        curr = self.head

        while count <= index:
            if curr == None:
                if count == index:
                    self.addAtTail(val)
                return

            if count == index:
                newNode = Node(val)

                previous = curr.previous
                previous.next = newNode

                newNode.previous = previous
                newNode.next = curr

                curr.previous = newNode
                break
            else:
                curr = curr.next
                count += 1

    def deleteAtIndex(self, index: int) -> None:
        count = 0

        if self.head is None:
            return

        curr = self.head

        while count <= index:
            if curr == None:
                return
                
            if index == 0:
                self.head = self.head.next

                if self.head is None:
                    self.tail = None
                return

            if count == index:
                if curr == self.tail:
                    previous = self.tail.previous
                    previous.next = None
                    self.tail = previous
                    return

                previous = curr.previous
                next = curr.next

                previous.next = next
                next.previous = previous
                break
            else:
                curr = curr.next
                count += 1
            

        
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)