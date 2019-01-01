#create Node
#create linked list



class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertHead(self,newNode):
        #data => Mathew, next=>None
        tempNode  = self.head
        self.head = newNode
        self.head.next = tempNode
        del tempNode

    def insert(self,newNode):
        if self.head is None:
            self.head = newNode
        else:
            #head=>John->Ben->Mathew->None
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode


    def printList(self):
        #head=>john->Ben->Mathew->None
        #if self.head is None:
        #    print"List is Empty"
        #    return
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next
#node => data, next

#FirstNode.data=>john, firstNode.next=>None
firstNode = Node("john")
linkedlist = LinkedList()
linkedlist.insert(firstNode)
secondNode = Node("Ben")
linkedlist.insert(secondNode)
thirdNode = Node("Mathew")
linkedlist.insert(thirdNode)
headNode = Node("satya")
linkedlist.insertHead(headNode)
linkedlist.printList()



