#node class
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
#linkedlist class
class LinkedList:
    def __init__(self):
        self.head=None
    #inserting nodes into linkedlist
    def insert(self,newnode):
        if self.head is None:
            self.head=newnode
            return
        lastnode=self.head
        while True:
            if lastnode.next is None:
                break
            lastnode=lastnode.next
        lastnode.next=newnode
    #printing elements of linkedlist
    def printllist(self):
        currentnode=self.head
        if self.head is None:
            print("linkedlist is empty")
        while True:
            if currentnode is None:
                break
            print(currentnode.data)
            currentnode=currentnode.next
    #function for reversing
    def reverse(self):
        if self.head is None:
            return
        self.recursive_reverse(self.head,None)
    #function which does recursion
    def recursive_reverse(self,currentnode,previousnode):
        if currentnode.next is None:
            self.head=currentnode
            currentnode.next=previousnode
            return
        nextnode=currentnode.next
        currentnode.next=previousnode
        self.recursive_reverse(nextnode,currentnode)
if __name__ == '__main__':
    llist=LinkedList()
    firstnode=Node(1)
    secondnode=Node(2)
    thirdnode=Node(3)
    fourthnode=Node(4)
    fifthnode=Node(5)
    llist.insert(firstnode)
    llist.insert(secondnode)
    llist.insert(thirdnode)
    llist.insert(fourthnode)
    llist.insert(fifthnode)
    print("linkedlist before reversing")
    llist.printllist()
    print("linkedlist after reversing")
    llist.reverse()
    llist.printllist()






