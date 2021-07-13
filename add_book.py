from find_book import *
import json


ISBN = "9780517884539"
# ISBN = "9789794030462"

def add_book(ISBN):

    title, series, authors = find_book(ISBN)

    with open('books.json', 'r+') as f:
        data = json.load(f)

        isbns = set()

        for book in data["books"]:
            if book["ISBN"] not in isbns:
                isbns.add(book["ISBN"])

        if ISBN not in isbns:
            new_book = {
                "ISBN": ISBN,
                "title": title,
                 "series": series,
                 "authors": authors
            }

            data["books"].append(new_book)

            f.seek(0)
            json.dump(data, f, indent=4)


    print(data["books"])

add_book(ISBN)