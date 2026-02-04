class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
    
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __str__(self):
        temp = self.head
        result = ""
        while temp:
            result += str(temp.value)
            if temp.next :
                result += ' => '
            temp = temp.next
        return result
            
        
    def append(self,value):
        node = Node(value)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
            
    def traversal(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
            


new = LinkedList()
new.append(5)
new.append(10)
new.append(66)
new.traversal()


# print(new.tail.value)
print(new)


        
    