from sqlalchemy import create_engine, select, Column, Integer, String, ForeignKey, select
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session, registry, relationship
import os

password = os.getenv("PASSWORD")

engine = create_engine(f'postgresql+psycopg2://postgres:{password}@localhost/library')

mapper_registry = registry()

Base = mapper_registry.generate_base()

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(length=50))
    last_name = Column(String(length=50))

    def __repr__(self):
        return "<Author(id={0}, firstname='{1}', lastname='{2}')>".format(self.id, self.first_name, self.last_name)

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String(length=100))
    num_pages = Column(Integer)

    def __repr__(self):
        return "<Book(id={0}, title='{1}')>".format(self.id, self.title)
        
class AuthorBooks(Base):
    __tablename__ = 'authorbooks'
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('authors.id'))
    book_id = Column(Integer, ForeignKey('books.id'))

    auhtor = relationship("Author")
    book = relationship("Book")

    def __repr__(self):
        return "<AuthorBook(id={0}, auhtor_id={1}, book_id={2})>".format(self.id, self.author_id, self.book_id)

Base.metadata.create_all(engine)

def add_book(title, number_of_pages, fname, lname):
    author = Author(first_name=fname, last_name=lname)
    book = Book(title=title, num_pages=number_of_pages) 

    with Session(engine) as session:
        exist_book = session.execute(select(Book).filter(Book.title==title, Book.num_pages==number_of_pages)).scalar()
        if exist_book is not None:
            print("Book exists!")
            return
        
        print("Book does not exist! adding it.")
        session.add(book)

        exist_author = session.execute(select(Author).filter(Author.first_name==fname, Author.last_name==lname)).scalar()
        if exist_author is not None:
            print("Author exists! not adding author.")
            session.flush()
            pairing=AuthorBooks(author_id=exist_author.id, book_id=book.id)
        else:
            print("Author does not exist! adding author")
            session.add(author)
            session.flush()
            pairing=AuthorBooks(author_id=author.id, book_id=book.id)

        session.add(pairing)
        session.commit()
        print(f"New pairing added: {str(pairing)}")

if __name__ == "__main__":
    print("Input new book:\n")
    title = input("Titlle of the book: ")
    number_of_pages = int(input("Number of pages: "))
    firstname = input("First name of the author: ")
    lastname = input("Last name of the author: ")
    print("Adding the new book..")
    add_book(title, number_of_pages, firstname, lastname)
    print("Done!")
