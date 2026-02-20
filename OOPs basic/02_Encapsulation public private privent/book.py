class Book:
    def __init__(self, title, author,category):

        self.title = title
        self.author = author
        self._category = category   # ✅ protected
        self.__available = True       # ✅ private
    
    def is_available(self):
        return self.__available
    
    def borrow_book(self):
        if self.__available:
            self.__available = False
            print(f"you have borrowed {self.title} by {self.author}")

        else:
            print(f"Sorry, '{self.title}' is currently not available.")

    def return_book(self):
        if not self.__available:
            self.__available = True
            print(f"Thank you for returning '{self.title}'")
        
        else:
            print(f"'{self.title}' was not borrowed.")

    def display(self):
        status = "Available" if self.__available else "Not Available"
        print(f"Book: {self.title} by {self.author} | Category: {self._category} | Status: {status}")

class ScienceBook(Book):
    def __init__(self, title, author):
        super().__init__(title, author, "Science")

    def show_category(self):
        print(f"This is a Science book. Category: {self._category}")

book1 = Book("The Alchemist", "Paulo Coelho", "Fiction")
book2 = ScienceBook("Quantum Physics", "Stephen Hawking")

book1.display()
book1.borrow_book()
book1.display()
book1.return_book()
print()

book2.display()
book2.show_category()
book2.borrow_book()
book2.return_book()
