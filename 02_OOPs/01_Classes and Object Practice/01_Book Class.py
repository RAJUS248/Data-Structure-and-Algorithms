class Book:

    def __init__(self,name,auother):
        self.name = name
        self.auother = auother

    
    def info(self):
        print(f"name of book is {self.name} and written by {self.auother}")

    
book = Book('1989','raja')
book.info()