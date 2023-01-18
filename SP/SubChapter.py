from Image import *
from Table import *
from Paragraph import *
class Subchapter:
    def __init__(self, name):
        self.name = name
        self.elements = []

    def print(self):
        print("Subchapter: " + self.name)
        for e in self.elements:
            e.print()

    def create_new_paragraph(self, s):
        paragraph = Paragraph(s)
        self.elements.append(paragraph)

    def create_new_image(self, s):
        image = Image(s)
        self.elements.append(image)

    def create_new_table(self, s):
        table = Table(s)
        self.elements.append(table)