from grupa import *
class An:
    grupe = []
    def __init__(self, nume):
        self.nume = nume

    def add(self, grupa):
        self.grupe.append(grupa)
    
    def __str__(self):
        str = self.nume
        return str