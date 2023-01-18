from Element import *

class Table(Element):
    def __init__(self, title):
        self.title = title

    def print(self):
        print("Table with Title: " + self.title)

    def add(self, e):
        pass

    def remove(self, e):
        pass

    def get(self, index):
        return None

    def accept(self, v):
        v.visit_table(self)