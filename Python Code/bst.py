class bst:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def printdata(root):
        if root == None:
            return
        if root.left != None:
            printdata(root.left)
        if root.right != None:
            printdata(root.right)
        print(root.left)
        print(root.right)
            

bs1=bst(2)
printdata(bs1)

