class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year
    def __eq__(self, other):
        return self.name == other.name and self.author == other.author and self.year == other.year