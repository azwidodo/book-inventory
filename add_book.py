from find_book import *
import pandas as pd


ISBN = "97805178845391"
# ISBN = "9789794030462"
# ISBN = "9780349142630"

print(find_book(ISBN))


def add_book(ISBN):

    title, series, authors = find_book(ISBN)

    df = pd.read_csv("books.csv")

    isbns = df["ISBN"].unique()

    if title != "None":
        if ISBN not in isbns:

            if not series:
                row = [title, "", authors]
            else:
                row = [title, series, authors]
