from semigrupa import *
class Grupa:
    semigrupe = []
    def __init__(self, nume):
        self.nume = nume
    def add(self, semigrupa):
        self.semigrupe.append(semigrupa)
    
    def __str__(self):
        str =self.nume
        return str
        