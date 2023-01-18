class Author(object):
    author = str()

    def __init__(self, author):
        self.author = author

    def print_(self):
        print ("Author: " + self.author)