# %%

import pandas as pd
import json
from find_book import *


data = []

to_add = []

with open("books.json", "r+") as f:
    books = json.load(f)

    for book in books["books"]:
        to_add.append(book["ISBN"])

with open("not_yet.txt", "r+") as f:
    for line in f:
        isbn = line.rstrip()
        to_add.append(isbn)

for isbn in to_add:
    title, series, authors = find_book(isbn)

    if title != "None":
        if not series:
            row = [isbn, title, "", authors]
        else:
            row = [isbn, title, series, authors]

        data.append(row)

df = pd.DataFrame(data, columns=["ISBN", "title", "series", "authors"])


# %%

df.to_csv("books.csv")

# %%
