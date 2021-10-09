import requests
from bs4 import BeautifulSoup


ISBN = "97805178845391"
# ISBN = "9781447220718"
# ISBN = "9789794030462"
# ISBN = "9781398505247"

url = f"http://goodreads.com/search?q={ISBN}"

page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

try:
    title_head = soup.find("h1", {"id": "bookTitle"})
    title_string = title_head.stripped_strings

    for text in title_string:
        title = text

except:
    title = "None"

try:
    authors_head = soup.find_all("a", {"class": "authorName"})

    authors = []
    for head in authors_head:
        authors.append(head.span.string)

except:
    authors = []

try:
    series_head = soup.find("h2", {"id": "bookSeries"})
    series_string = series_head.stripped_strings

    series = []
    for text in series_string:
        series.append(text)

except:
    series = []


# print(title_head)
# print(authors_head)
# print(series_head)

print(title)
print(authors)
print(series)
