from SubChapter import SubChapter
from typing import List

class Chapter:
    def __init__(self, ch: str):
        self.ch = ch
        self.subChapters = []

    def print(self):
        print(self.ch)
        for el in self.subChapters:
            el.print()

    def createSubChapter(self, s: str) -> int:
        self.subChapters.append(SubChapter(s))
        return len(self.subChapters) - 1

    def getSubChapter(self, i: int) -> 'SubChapter':
        return self.subChapters[i]