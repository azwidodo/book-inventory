from tkinter import *
from find_book_Edge import *
# from find_book_Chrome import *
import json


root = Tk()
root.title("Book Inventory")
root.geometry("600x600")

# entry and buttons
frame1 = Frame(root)
frame1.pack()

# book info
frame2 = Frame(root)
frame2.pack()

# book database
frame3 = Frame(root)
frame3.pack()


isbn_entry = Entry(frame1)
isbn_entry.grid(row=0, column=2, columnspan=2, padx=20, pady=(10, 0))
isbn_label = Label(frame1, text="Enter Book ISBN: ").grid(
    row=0, column=0, columnspan=2, padx=10, pady=(10, 0))


def show_book():
    for widget in frame2.winfo_children():
        widget.destroy()

    isbn = str(isbn_entry.get())

    if find_book(isbn):
        title, series, authors = find_book(isbn)

        Label(frame2, text="ISBN: ").grid(row=0, column=0, padx=10)
        Label(frame2, text="Title: ").grid(row=1, column=0, padx=10)
        Label(frame2, text="Series: ").grid(row=2, column=0, padx=10)
        Label(frame2, text="Authors: ").grid(row=3, column=0, padx=10)

        Label(frame2, text=f"{isbn}").grid(
            row=0, column=1, columnspan=6, sticky="w")
        Label(frame2, text=f"{title}").grid(
            row=1, column=1, columnspan=6, sticky="w")
        Label(frame2, text=f"{series}").grid(
            row=2, column=1, columnspan=6, sticky="w")
        Label(frame2, text=f"{authors}").grid(
            row=3, column=1, columnspan=6, sticky="w")

    else:
        Label(frame2, text="Book not found.", fg="#f00").grid(
            row=0, column=0, padx=10)


def add_book():

    isbn = str(isbn_entry.get())
    show_book()

    if find_book(isbn):
        title, series, authors = find_book(isbn)

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

                Label(frame2, text="Book added to database!", fg="#0f0").grid(
                    row=4, column=0, columnspan=4)

            else:
                Label(frame2, text="Book already exists in database!", fg="#f00").grid(
                    row=4, column=0, columnspan=4)


def show_database():
    with open('books.json', 'r+') as f:
        data = json.load(f)

    Label(frame3, text="No. ISBN, Title, Series, Authors").grid(
        row=0, column=0, columnspan=10, padx=10, pady=(10, 0), sticky="w")

    for i, book in enumerate(data["books"]):

        Label(frame3, text=f"{i+1}. {book['ISBN']}, {book['title']}, {book['series']}, {book['authors']}").grid(
            row=1 + i, column=0, columnspan=10, padx=10, sticky="w")


find_button = Button(frame1, text="Find Book", command=show_book).grid(
    row=1, column=0, columnspan=2, pady=10, ipadx=10)

add_button = Button(frame1, text="Add Book to Database", command=add_book).grid(
    row=1, column=2, columnspan=2, pady=5)

show_db_btn = Button(frame1, text="Show Book Database", command=show_database).grid(
    row=3, column=0, columnspan=2, pady=5)

root.mainloop()
