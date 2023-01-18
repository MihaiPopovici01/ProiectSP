from Paragraph import *
from AlignStrategy import *

class AlignLeft(AlignStrategy):
    par = Paragraph()

    def __init__(self):
        super(AlignLeft, self).__init__()

    def render(self, x):
        print (x.name + "####")