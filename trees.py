class TreeNode:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
        
        
    
        
        
t1 = TreeNode("drinks")
t2 = TreeNode("hot")
t3 = TreeNode("cold")
t1.left = t2
t1.right = t3
# print(t1.left.data)
        
# t1.preorder()
def preorder(node):
    if not node:
        return
    print(node.data)
    preorder(node.left)
    preorder(node.right)
        

def inorder(node):
    if not node:
        return
    inorder(node.left)
    print(node.data)
    inorder(node.right)
    
def postorder(node):
    if not node:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data)
# preorder(t1)
# inorder(t1)
# postorder(t1)