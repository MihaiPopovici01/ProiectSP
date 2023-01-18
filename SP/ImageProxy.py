from Pictures import *
from Element import *
from Image import *

class ImageProxy(Pictures, Element):
    def __init__(self, url):
        self.url = url
        self.real_img = None

    def load_image(self):
        if self.real_img is None:
            self.real_img = Image(self.url)

    def url(self):
        return self.url

    def print(self):
        self.load_image()
        self.real_img.print()

    def add(self, e):
        pass

    def remove(self, e):
        pass

    def get(self, index):
        pass

    def accept(self, v):
        v.visit_image_proxy(self)