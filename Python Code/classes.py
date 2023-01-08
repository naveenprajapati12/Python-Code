class computer:
    model=10
    def __init__(self,a,b):
        print('i am a constructor')
        self.verson=a
        self.price=b
    def config(self):
        print("verson of computer is---> {}  and price of that computer----> {} ".format(self.verson,self.price))
        
    def swap(self,a,b):
        a,b=b,a
        print(a,b)
           
d1=computer('new',650000)
d1.config()
d1.swap(5, 2)

