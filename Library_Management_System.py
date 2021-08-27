class Library:
    def __init__(self,list,name):
        self.booklist=list
        self.name=name
        self.lendDict={}

    def displayBooks(self):
        print(f"The books present in library : {self.name}")
        for book in self.booklist:
            print(book)

    def lendBook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Book taken successfully")
        else:
            print(f"Book is issued to {self.lendDict[book]}")

    def addBooks(self,book):
        self.booklist.append(book)
        print("Book has been added in list")

    def returnBook(self,book):
        self.booklist.remove(book)

if __name__ == '__main__' :
    yds=Library(['js','cpp','c','ds'], 'apni_library')

while(True):
    print(f"Welcome to the {yds.name} library press to continue")
    print("1. Display")
    print("2. add")
    print("3. lend")
    print("4. return book\n")
    user=int(input())

    if user==1:
        yds.displayBooks()
    elif user==2:
        book=input("enter the name to add")
        yds.addBooks(book)
    elif user==3:
        book=input("enter book name to lend")
        user=input("enter your name")
        yds.lendBook(user,book)
    elif user==4:
        book=input("enter the book you want to return")
        yds.returnBook(book)
    else:
        print("Invalid !!!")
    print("press q to quit & c to continue")
    choice=input()
    if choice=='c':
        continue
    if choice=='q':
        exit()