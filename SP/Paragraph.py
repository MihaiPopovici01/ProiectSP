from Element import *

class Paragraph(Element):
    def __init__(self, name):
        self.name = name
        self.x = None

    def set_align_strategy(self, strat):
        self.x = strat

    def print(self):
        if self.x is None:
            print(self.name)
        else:
            self.x.render(Paragraph(self.name))

    def add(self, e):
        pass

    def remove(self, e):
        pass

    def get(self, index):
        return None

    def accept(self, v):
        v.visit_paragraph(self)