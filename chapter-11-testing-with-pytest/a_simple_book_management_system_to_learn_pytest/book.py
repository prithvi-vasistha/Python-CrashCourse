class Book:
    def __init__(self, name, author, copies):
        self.name = name
        self.author = author 
        self.copy = copies

    def is_available(self):
        if self.copy>0:
            return True
        else:
            return False
        
    def borrow(self, bookname):
        if self.name == bookname:
            if self.copy>0:
                self.copy -= 1
                return(self.copy)
            else:
                raise Exception("No books available at the current moment")
        else:
            raise Exception("Unknown book")
    
    def return_book(self, bookname):
        if self.name == bookname:
            self.copy += 1
            return(self.copy)
        else:
            raise Exception("Unknown book")
