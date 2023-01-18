class TableContent:
    def __init__(self):
        pass

    def accept(self, v):
        v.visit_table_content(self)