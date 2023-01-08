class node:
  def __init__(self,data=None):
    self.data=data
    self.nextval=None
class linkedlist:
  def __init__(self):
    self.headval=None
  def printlist(self):
    printval=self.headval
    while printval is not None:
      print(printval.data)
      printval=printval.nextval
      #insert at begining
  def insertatbegining(self,newdata):
    newnode=node(newdata)
    newnode.nextval=self.headval
    self.headval=newnode
     #insert at mid
  def insertatmiddle(self,mid_data,newdata):
    if mid_data is None:
        print('The node is adsent')
        return
    newnode=node(newdata)
    newnode.nextval=mid_data.nextval
    mid_data.nextval=newnode
    #insert at end
  def insertatend(self, newdata):
    NewNode = node(newdata)
    if self.headval is None:
        self.headval = NewNode
        return
    last = self.headval
    while(last.nextval):
        last = last.nextval
        last.nextval=NewNode
list=linkedlist()
e1=node('sun')
list.headval=e1
e2=node('tue')
e1.nextval=e2
list.headval.nextval=e2
e1.nextval=e2
e3=None
e2.nextval=e3
list.insertatbegining('sat')
list.insertatmiddle(list.headval.nextval,"mon")
list.insertatend("wed")
list.printlist()
