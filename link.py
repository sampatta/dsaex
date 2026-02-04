class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
    
class LinkList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __str__(self):
        temp = self.head
        res = ""
        while temp :
            res += str(temp.value)
            if temp.next:
                res+= "=>"
            temp = temp.next
        return res
    
    def append(self,value):
        node = Node(value)
        if self.head == None:
            self.head = node
            self.tail =node
        else:
            self.tail.next = node
            self.tail = node
            
    
# LinkList(4)
a =LinkList()
a.append(6)
a.append(7)
a.append(5)
print(a)
 