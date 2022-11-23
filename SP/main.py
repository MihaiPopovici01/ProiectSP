from Book import *
from Author import *

Book1 = Book("Nume")
Auth1 = Author("Ionica")
Book1.addAuthor(Auth1)
Ch1 = Book1.chapters[Book1.addChapter("P1")]
print(Ch1.name)


