class Library:
    def __init__(self, list):
        self.lst = []
    def __add__(self, other):
        self.lst.append(other)
