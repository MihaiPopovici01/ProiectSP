class Chapter:
    def __init__(self, name):
        self.name = name
        self.subChapters = []
    def __str__(self):
        return self.name
        