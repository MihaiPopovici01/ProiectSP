from Paragraph import *
from AlignStrategy import *

class AlignCenter(AlignStrategy):
    
    par = Paragraph()

    def __init__(self):
        super(AlignCenter, self).__init__()

    def render(self, x):
        print ("####" + x.name + "####")