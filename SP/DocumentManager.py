class DocumentManager:
    instance = None
    def __init__(self):
        if DocumentManager.instance is None:
            DocumentManager.instance = self
            self.myBook = None
    @staticmethod
    def getInstance():
        return DocumentManager.instance

    def getBook(self):
        return self.myBook

    def setBook(self, myBook):
        self.myBook = myBook