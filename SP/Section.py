from Element import *

class Section(Element):
    def __init__(self, title):
        self.title = title
        self.elements = []

    def print(self):
        print(self.title)
        for element in self.elements:
            element.print()

    def add(self, e):
        self.elements.append(e)

    def remove(self, e):
        self.elements.remove(e)

    def get(self, index):
        return self.elements[index]

    def accept(self, v):
        v.visit_section(self)