import requests
from bs4 import BeautifulSoup


# ISBN = "9780008309008"
ISBN = "9780517884539"

url = f"https://www.abebooks.com/servlet/SearchResults?sts=t&isbn={ISBN}"

page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

result = soup.find("li", {"id": "book-1"})
heading = result.find("h2", {"class": "title"})
heading_url = heading.find("a")
book_title = heading_url.span.string
p_author = result.find("p", {"class": "author"})
book_author = p_author.strong.string

print(book_title)
print(book_author)