from Section import *

class Book(Section):
    authors = []

    def __init__(self, title):
        super(Book, self).__init__(title)

    def addContent(self, content):
        self.add(content)

    def addAuthor(self, author):
        self.authors.append(author)

    def print_(self):
        print ("Authors:")
        for a in self.authors:
            a.print_()
        super(Book, self).print_()

    def accept(self, v):
        v.visitBook(self)