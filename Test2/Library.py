class Library:
    def __init__(self):
        self.__books =[]
        self.start()


    def start(self):
        print("Welcome to BookShop -----------")
        choice = 0
        while choice!= 5 :
            print(" please pick a choice :"
                  "\n 1. Add new book \n 2. Remove a book \n 3. Show all books \n 4.Update a book \n 5.exit ")

            choice = int(input('>'))
            if (choice==1):
                bookName = input("please enter the book's name :   ")
                self.addBook(bookName)
            elif choice ==2:

                self.checkBook(1)


            elif choice ==3 :
                self.showBooks()

            elif choice ==4 :

                self.checkBook(2)

            elif choice == 5:
                print("exiting...")

            else:
                print("unsupported choice")




    def addBook(self, bookName):
        if(len(self.__books)<=10 and not bookName.isnumeric()):
            if(bookName not in self.__books):
             self.__books.append(bookName)
             print('added successfully')
        else:
            print("You can't add more than 10 books!")




    def removeBook(self , bookName):

          self.__books.remove(bookName)
          print("removed successfully ------")


    def showBooks(self)  :
        for book in self.__books:
            print(book)

    def updateBook(self , bookName):
        try :
            index = self.__books.index(bookName)
            self.__books.remove(bookName)
            newBook = input('please enter a new Book name : ')
            if not newBook.isnumeric():
                self.__books.insert(index , newBook)
                print('---updated successfully')


            else :
                print('please enter a string name')

        except IndexError :

            print("please enter a name that exists!")


    def checkBook(self , num):
        while True:
            bookName = input("please enter the name of the book    :   ")
            if (bookName in self.__books ):
                if( num ==1):
                  self.removeBook(bookName)

                elif num==2:
                    self.updateBook(bookName)

                break


            else:
                print('name doesn\'t exist !')