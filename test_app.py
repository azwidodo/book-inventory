from tkinter import *
from find_book_Edge import *
# from find_book_Chrome import *
import json

root = Tk()
root.title("Book Inventory")
root.geometry("600x600")

isbn_entry = Entry(root)
isbn_entry.grid(row=0, column=2, columnspan=2, padx=20, pady=(10, 0))
isbn_label = Label(root, text="Enter Book ISBN: ").grid(
    row=0, column=0, columnspan=2, padx=10, pady=(10, 0))


def show_book():

    isbn = str(isbn_entry.get())
    title, series, authors = find_book(isbn)

    Label(root, text="ISBN: ").grid(row=4, column=0, padx=10)
    Label(root, text="Title: ").grid(row=5, column=0, padx=10)
    Label(root, text="Series: ").grid(row=6, column=0, padx=10)
    Label(root, text="Authors: ").grid(row=7, column=0, padx=10)

    Label(root, text=f"{isbn}").grid(row=4, column=1, columnspan=6, sticky="w")
    Label(root, text=f"{title}").grid(
        row=5, column=1, columnspan=6, sticky="w")
    Label(root, text=f"{series}").grid(
        row=6, column=1, columnspan=6, sticky="w")
    Label(root, text=f"{authors}").grid(
        row=7, column=1, columnspan=6, sticky="w")


def add_book():

    isbn = str(isbn_entry.get())
    title, series, authors = find_book(isbn)
    show_book()

    with open('books.json', 'r+') as f:
        data = json.load(f)

        isbns = set()

        for book in data["books"]:
            if book["ISBN"] not in isbns:
                isbns.add(book["ISBN"])

        if isbn not in isbns:
            new_book = {
                "ISBN": isbn,
                "title": title,
                "series": series,
                "authors": authors
            }

            data["books"].append(new_book)

            f.seek(0)
            json.dump(data, f, indent=4)

            Label(root, text="Book added to database!", fg="#0f0").grid(
                row=8, column=0, columnspan=4)

        else:
            Label(root, text="Book already exists in database!", fg="#f00").grid(
                row=8, column=0, columnspan=4)


def show_database():
    with open('books.json', 'r+') as f:
        data = json.load(f)

    Label(root, text="No. ISBN, Title, Series, Authors").grid(
        row=9, column=0, columnspan=10, padx=10, pady=(10, 0), sticky="w")

    for i, book in enumerate(data["books"]):

        Label(root, text=f"{i+1}. {book['ISBN']}, {book['title']}, {book['series']}, {book['authors']}").grid(
            row=10 + i, column=0, columnspan=10, padx=10, sticky="w")


find_button = Button(root, text="Find Book", command=show_book).grid(
    row=1, column=0, columnspan=2, pady=10, ipadx=10)

add_button = Button(root, text="Add Book to Database", command=add_book).grid(
    row=1, column=2, columnspan=2, pady=5)

show_db_btn = Button(root, text="Show Book Database", command=show_database).grid(
    row=3, column=0, columnspan=2, pady=5)


root.mainloop()
