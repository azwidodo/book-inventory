from tkinter import *
from find_book_Edge import *
# from find_book_Chrome import *
import json

root = Tk()
root.title("Book Inventory")
root.geometry("600x600")

isbn_entry = Entry(root)
isbn_entry.grid(row=0, column=2, columnspan=2, padx=20, pady=(10,0))
isbn_label = Label(root, text="Enter Book ISBN: ").grid(row=0, column=0, columnspan=2, padx=10, pady=(10,0))



def find():

    isbn = str(isbn_entry.get())
    title, series, authors = find_book(isbn)

    shown = f"ISBN: {isbn} \n \
            Title: {title} \n \
            Series: {series} \n \
            Authors: {authors}"

    shown_label = Label(root, text=shown).grid(row=4, column=0, columnspan=4)



find_button = Button(root, text="Find Book", command=find).grid(row=1, column=0, columnspan=2, pady=10, ipadx=10)

add_button = Button(root, text="Add Book to Database").grid(row=1, column=2, columnspan=2, pady=5)

show_db_btn = Button(root, text="Show Book Database").grid(row=3, column=0, columnspan=2, pady=5)


root.mainloop()