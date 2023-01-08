class student:
    def __init__(self1,h,e,m):
        self1.hindi=h
        self1.english=e
        self1.maths=m
    def __gt__(self,other) -> bool:
        p = self.hindi+self.english+self.maths
        q = other.hindi+other.english+other.maths
        if p>q:
            return True
        else:
            return False
    def __eq__(self,oth) -> bool:
        p = self.hindi+self.english+self.maths
        q = oth.hindi+oth.english+oth.maths
        if p==q:
            return True
        else:
            return False
s1=student(5,10,100)
s2=student(5,10,100)
if s1>s2:
    print('s1 won')
elif s1==s2:
    print('equal')
else:
    print('s2 won')

        
