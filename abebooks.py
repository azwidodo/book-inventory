import requests
from bs4 import BeautifulSoup


ISBN = "9780008309008"
# ISBN = "9780517884539"
# ISBN = "9781447220718"
# ISBN = "9789794030462"

url = f"https://www.abebooks.com/servlet/SearchResults?sts=t&isbn={ISBN}"

page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

result = soup.find("li", {"id": "book-1"})
heading = result.find("h2", {"class": "title"})
heading_url = heading.find("a")
book_title = heading_url.span.string
p_author = result.find("p", {"class": "author"})
book_author = p_author.strong.string
book_series = ""

authors = book_author.split(",")

print(book_title)
print(book_author)
print(authors)