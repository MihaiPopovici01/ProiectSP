from Paragraph import *
from AlignStrategy import *

class AlignRight(AlignStrategy):
    par = Paragraph()

    def __init__(self):
        super(AlignRight, self).__init__()

    def render(self, x):
        print ("+++++" + x.name)