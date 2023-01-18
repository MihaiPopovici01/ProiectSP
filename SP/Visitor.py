from abc import ABC, abstractmethod

class Visitor(ABC):
    @abstractmethod
    def visit_book(self, book):
        pass

    @abstractmethod
    def visit_section(self, section):
        pass

    @abstractmethod
    def visit_table_content(self, table_content):
        pass

    @abstractmethod
    def visit_paragraph(self, paragraph):
        pass

    @abstractmethod
    def visit_image_proxy(self, image_proxy):
        pass

    @abstractmethod
    def visit_image(self, image):
        pass

    @abstractmethod
    def visit_table(self, table):
        pass