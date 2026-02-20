class Book:

    def __init__(self, title, author):

        self.title = title
        self.author = author

    def info(self):

        print(f"Book: {self.title} by {self.author}")
        
book1 = Book("OOPs" ,"raja" )
book2 = Book("matric 1989", "jyoti baradur")

book1.info()
book2.info()


