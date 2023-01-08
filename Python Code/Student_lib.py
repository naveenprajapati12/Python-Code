class Book:
        def __init__(self,t,a,c,n):

            self.title=t
            self.author=a
            self.cost=c
            self.num=n
            
            
        def display(self):
             print('book no. is : ',self.num)  
                
                
if __name__=='__main__':
 print('\n\n\t\t\t***✌️✌️✌️Welcome to our library Management System✌️✌️✌️***\n\n')

List_books=[]
book_num=[]
students=[]
while(True):
     print("\t\t \n\n")
     print("\t\t press 1 -> Add new book")
     print("\t\t press 2 -> Delete book")
     print("\t\t press 3 -> Show all books")
     print("\t\t press 4 -> Add new student")
     print("\t\t press 5 -> To Delete student")
     print("\t\t press 6 -> Issue new book")
     print("\t\t press 7 -> Return books")
     print("\t\t press 8 -> Exit form lib ")
          
     key = input("choose option ")

     if key=='1':
                t=input('Enter the Title name : ')
                a=input('Enter the Author name : ')
                c=input('Enter the cost of book :')
                n=input('Enter the no of book :')
                book_num.append(n)
                List_books.append(Book(t,a,c,n))
                print("Book added sucussfully")                
                continue
     elif key =='2':
             List_books.pop()
             print('recently added book deleted...')
             print('now the list is ')
             for j in List_books:
                      print('Title is :',j.title)
                      print('author is :',j.author)
                      print('cost is :',j.cost)
                     
                      continue 
                        
     elif key =='3':
                print('***Show All Book***')
                for j in List_books:
                        print('Title is :',j.title)
                        print('author is :',j.author)
                        print('cost is :',j.cost)
                        
                        continue      
     elif key =='4':
          print('Add new student..')
          std=input('Enter student name...')
          students.append(std)
          print('Student added sucessfully..')
          
          print('\n\n')
          print('list of students...')
          for i in students:
                  print(i)



     elif key =='5':
                students.pop()
                print('recently added student deleted...')
                print('now the list is ')

                for i in students:
                        print(i)
                print('student removed sucessfully...')
                continue



     elif key =='6':
                flag=0
                flag2=0
                num=input('Enter book number...')
                by_issue=input('Enter student name...')
                for i in students:
                        if i == by_issue:
                                flag=1
                for j in book_num:
                        if j== num:
                                flag2=1  

                if flag==1 and flag2==1:
                        print('Book issued ')
                else:
                        print('Book not available.')         
                
                continue
                        




     elif key =='7':
                return_book=input('Enter the book name...')
                for_issue=input('Enter the student name...')

                List_books.append(return_book)

                print("returned succesfully...")
                        
                
                
     elif key=='8':
         print('Now you out of library system')
         break
     else:
        print('you Entered wrong key: try again....')
        continue
 


