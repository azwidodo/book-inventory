import requests
import os
import json


ISBN = "9780349142630"
API_KEY = os.environ["GBOOKS_API_KEY"]

response = requests.get(
    "https://www.googleapis.com/books/v1/volumes?q=flowers+inauthor:keyes")
book_data = json.load(response)

print(book_data)
