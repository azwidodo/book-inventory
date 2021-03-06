import requests
from bs4 import BeautifulSoup
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
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)

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