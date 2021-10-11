from find_book import *
import pandas as pd
import re


ISBN = "9781839403705"

# print(find_book(ISBN))


def add_book(isbn):

    title, series, authors = find_book(isbn)

    df = pd.read_csv("books.csv")

    isbns = set(df["ISBN"].unique())

    if title != "None":
        if int(isbn) not in isbns:

            if not series:
                row = pd.DataFrame([[isbn, title, "", authors]], columns=[
                                   "ISBN", "title", "series", "authors"])

            else:
                ser = re.search(r"\((.*?)\)", series[0]).group(1)
                row = pd.DataFrame([[isbn, title, ser, authors]], columns=[
                                   "ISBN", "title", "series", "authors"])

            df = df.append(row, ignore_index=True)

            added = 0  # book has been added

        else:
            added = 1  # book already exists

    else:
        added = 2  # book is not found

    df.to_csv("books.csv", index=False)

    return title, series, authors, added


t, s, a, ad = add_book(ISBN)
