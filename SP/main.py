from Book import *
from Author import *
from DocumentManager import *
from Paragraph import *



my_book = Book("Carticica")
DocumentManager.get_instance().set_book(my_book)
me = Author("Ionut")
my_book.add_author(me)
cap1 = Section("Capitolul 1")
my_book.add_content(cap1)
p1 = Paragraph("Paragraph 1")
cap1.add(p1)
p2 = Paragraph("Paragraph 2")
cap1.add(p2)
p3 = Paragraph("Paragraph 3")
cap1.add(p3)
p4 = Paragraph("Paragraph 4")
cap1.add(p4)
        

@staticmethod
def printing():
    DocumentManager.get_instance().get_book().print()


