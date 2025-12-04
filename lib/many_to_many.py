class Author:
    # Keep track of every Author object created
    all = []

    def __init__(self, name):
        # name is a string
        self.name = name
        Author.all.append(self)

    def contracts(self):
        #Return all Contract objects that belong to this author
        
        related = []
        for contract in Contract.all:
            if contract.author is self:
                related.append(contract)
        return related

    def books(self):
        #Return all Book objects related to this author through contracts
       
        books_list = []
        for contract in Contract.all:
            if contract.author is self:
                if contract.book not in books_list:
                    books_list.append(contract.book)
        return books_list

    def sign_contract(self, book, date, royalties):
       #Create a new contract between this author and a book
    
        return Contract(self, book, date, royalties)

    def total_royalties(self):
       # Add up all royalties from this author's contracts
       
        total = 0
        for contract in self.contracts():
            total += contract.royalties
        return total


class Book:
    # Keep track of every Book object created
    all = []

    def __init__(self, title):
        # title is a string
        self.title = title
        Book.all.append(self)

    def contracts(self):
        #Return all Contract objects where this book is part of the contract
       
        related = []
        for contract in Contract.all:
            if contract.book is self:
                related.append(contract)
        return related

    def authors(self):
       #Return all Author objects connected to this book through contracts
    
        authors_list = []
        for contract in Contract.all:
            if contract.book is self:
                if contract.author not in authors_list:
                    authors_list.append(contract.author)
        return authors_list



class Contract:
    # Keep track of every Contract object created
    all = []

    def __init__(self, author, book, date, royalties):
        # Assign using property setters for validation
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)

    # author property
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("author must be an instance of Author")
        self._author = value

    # book property
    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("book must be an instance of Book")
        self._book = value

    # date property 
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("date must be a string")
        self._date = value

    # royalties property
    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception("royalties must be an integer")
        self._royalties = value

    #class method
    @classmethod
    def contracts_by_date(cls, date):
        # Return all contracts with the given date
        
        return [c for c in cls.all if c.date == date]