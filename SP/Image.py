import time
from Element import *

class Image(Element):
    def __init__(self, url):
        self.url = url

        time.sleep(5)
        image_content = None

    def print(self):
        print("Image with url: " + self.url)

    def add(self, e):
        pass

    def remove(self, e):
        pass

    def get(self, index):
        pass

    def accept(self, v):
        v.visit_image(self)