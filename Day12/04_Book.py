class Book:
    def __init__(self, title, author, price):
        self.btitle = title
        self.bauthor = author
        self.bprice = price
    def display_info(self):
        print("Book name:",self.btitle)
        print("Author name:",self.bauthor)
        print("Book price:",self.bprice)
b1 = Book("Mahatma Gandhi Autobiography", "Mahatama Gandhi", 300)
b2 = Book("God of Small Things", "Arundhati Roy", 250)
b1.display_info()
b2.display_info()