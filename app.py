from tkinter import *
from find_book import *
from add_book import *
import pandas as pd


root = Tk()
root.title("Book Inventory")
root.geometry("600x750")

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


def find_book_tk():
    for widget in frame2.winfo_children():
        widget.destroy()

    isbn = str(isbn_entry.get())
    title, series, authors = find_book(isbn)

    if title != "None":

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


def add_book_tk():
    for widget in frame2.winfo_children():
        widget.destroy()

    isbn = str(isbn_entry.get())
    title, series, authors, added = add_book(isbn)

    if added == 0:
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

        Label(frame2, text="Book added to database!", fg="#0f0").grid(
            row=4, column=0, columnspan=4)

    elif added == 1:
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

        Label(frame2, text="Book already exists in database!", fg="#f00").grid(
            row=4, column=0, columnspan=4)

    else:
        Label(frame2, text="Book not found.", fg="#f00").grid(
            row=4, column=0, columnspan=4)


def show_database():
    df = pd.read_csv("books.csv")

    # pd.set_option('display.width', 1000)
    # pd.set_option('display.max_columns', 2)
    # print(df.iloc[:, 0:2].tail(10))

    data = df.iloc[:, 0:2].tail(10).to_string()
    data_array = data.splitlines()

    for i in range(11):
        str = " ".join(data_array[i].split())
        Label(frame3, text=str).grid(row=i, column=0,
                                     columnspan=10, padx=10, pady=10, sticky="w")


find_button = Button(frame1, text="Find Book", command=find_book_tk).grid(
    row=1, column=0, columnspan=2, pady=10, ipadx=10)

add_button = Button(frame1, text="Add Book to Database", command=add_book_tk).grid(
    row=1, column=2, columnspan=2, pady=5)

show_db_btn = Button(frame1, text="Show Book Database", command=show_database).grid(
    row=3, column=0, columnspan=2, pady=5)

root.mainloop()
