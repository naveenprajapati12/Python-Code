class node:
    def __init__(self,data):
        self.data=data
        self.nextval=None


class linklist:
    def __init__(self):
        self.headvalue=None
    def printlist(self):
        printval = self.headvalue
        while printval is not None:
            print(printval.data)
            printval = printval.nextval  
    


list = linklist()
e1 = node('sun')
list.headvalue = e1 
e2=node('Mon')
list.headvalue = e2

list.printlist()
    