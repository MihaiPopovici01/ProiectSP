from abc import ABC, abstractmethod

class Pictures(ABC):
    @abstractmethod
    def url(self):
        pass