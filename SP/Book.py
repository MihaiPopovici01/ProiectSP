from Author import *
from Chapter import *

class Book:
    def __init__(self, name):
        self.name = name
        self.chapters = []
        
    def addAuthor(self, author):
        self.author = author.name
    
    def addChapter(self, name):
        ch = Chapter(name)
        self.chapters.append(ch)
        return len(self.chapters) - 1

    def __str__(self):
        str ="Numele cartii: " + self.name + "\nNumele autorului: " + self.author
        return str