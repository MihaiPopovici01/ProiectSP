import random

class BookStats:
    def __init__(self):
        self.imgCount = 0
        self.tableCount = 0
        self.paraCount = 0
        self.contorImg = 1
        self.contorTable = 1
        self.contorPara = 1

    def RNG(self):
        rand = random.Random()
        upperbound = 30
        return rand.randint(0, upperbound)

    def visitBook(self, b):
        for child in b.elements:
            child.accept(self)

    def visitSection(self, s):
        for child in s.elements:
            child.accept(self)

    def visitTableContent(self, tc):
        pass

    def visitParagraph(self, p):
        print(f"Paragraph {self.contorPara} page {self.RNG()}")
        self.paraCount += 1
        self.contorPara += 1

    def visitImageProxy(self, imgP):
        print(f"Image Proxy {self.contorImg} page {self.RNG()}")
        self.imgCount += 1
        self.contorImg += 1

    def visitImage(self, img):
        print(f"Image {self.contorImg} page {self.RNG()}")
        self.imgCount += 1

    def visitTable(self, t):
        print(f"Table {self.contorTable} page {self.RNG()}")
        self.tableCount += 1
        self.contorTable += 1

    def printStats(self):
        print("Book Stats")
        print(f" Number of images: {self.imgCount}")
        print(f" Number of tables: {self.tableCount}")
        print(f" Number of paragraphs: {self.paraCount}")