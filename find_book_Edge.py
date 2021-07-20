import requests
from bs4 import BeautifulSoup
from msedge.selenium_tools import Edge, EdgeOptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def find_book(ISBN):
    book_title, book_series, book_author = find_on_abebooks(ISBN)

    if book_title == None:
        book_title2, book_series2, book_author2 = find_on_goodreads(ISBN)

        if book_title2 == None:
            return "Not found"
        else:
            return book_title2, book_series2, book_author2

    return book_title, book_series, book_author


def find_on_goodreads(ISBN):
    # Launch Microsoft Edge (Chromium)
    PATH = "/Users/azw/Pictures/Programming/book-inventory/edgedriver_mac64/msedgedriver"

    options = EdgeOptions()
    options.use_chromium = True
    options.add_argument("headless")
    options.set_capability("platform", "MAC")

    driver = Edge(executable_path=PATH, options=options)

    driver.get("https://www.goodreads.com/")

    search = driver.find_element_by_name("query")
    search.clear()
    search.send_keys(ISBN)
    search.send_keys(Keys.RETURN)

    try:
        title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "bookTitle"))
        )
        series = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "bookSeries"))
        )
        authors = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "bookAuthors"))
        )

        book_title = title.text
        book_series = series.text
        author = authors.text[3:]
        book_author = author.split(",")

        if book_series == "":
            book_series = None

        return book_title, book_series, book_author

    except:
        book_title = None
        book_series = None
        book_author = None

        return book_title, book_series, book_author

    # time.sleep(5)
    driver.quit()


def find_on_abebooks(ISBN):
    url = f"https://www.abebooks.com/servlet/SearchResults?sts=t&isbn={ISBN}"

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    try:
        result = soup.find("li", {"id": "book-1"})
        heading = result.find("h2", {"class": "title"})
        heading_url = heading.find("a")
        book_title = heading_url.span.string
        p_author = result.find("p", {"class": "author"})
        author = p_author.strong.string
        book_author = author.split(",")
        book_series = None

        return book_title, book_series, book_author

    except:
        book_title = None
        book_series = None
        book_author = None

        return book_title, book_series, book_author


# THIS THREAD SAVED ME
# https://travis-ci.community/t/runtime-for-releases-of-edge-and-msedgedriver-with-python/11552


# DESIRED_CAP = {"os": "OS X",
#                "os_version": "Big Sur",
#                "browser": "Edge",
#                "browser_version": "90.0",
#                "browserstack.local": "false",
#                "browserstack.selenium_version": "3.141.0"
#                }
# driver = webdriver.Edge(executable_path=PATH,
#                         capabilities=DESIRED_CAP, options=options)
