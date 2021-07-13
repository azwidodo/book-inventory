from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Launch Microsoft Edge (Chromium)
# PATH = "C:\Program Files (x86)\msedgedriver.exe"
# options = EdgeOptions()
# options.use_chromium = True
# driver = Edge(executable_path=PATH, options=options)

ISBN = "9780517884539"
# ISBN = "9781447220718"

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
    book_author = authors.text[3:]
    
    
    
except:
    print("Book Not Found")


# time.sleep(5)
driver.quit()