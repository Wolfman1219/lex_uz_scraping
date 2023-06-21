from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import re
# Set the path to the Firefox driver executable
webdriver_path = 'geckodriver.exe'
binary_path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
# Set up the Firefox options
firefox_options = Options()
# firefox_options.add_argument('--headless')  
# Run Firefox in headless mode (without GUI)
firefox_options.binary_location = binary_path
firefox_options.add_argument('--no-sandbox')

# Start the Firefox WebDriver
driver = webdriver.Firefox(service=Service(webdriver_path), options=firefox_options)

# Load the web page using Selenium

# url = 'https://lex.uz/uz/classifiers/6131'  # Replace with the URL of the web page you want to scrape

s= 0
def writing_links(url):
    driver.get(url)


    elements = driver.find_elements(By.XPATH,"//i[@class=\"fas fa-plus\"]")
    # elements = list(elements)
    for element in elements: 
        element = element.click()


    # Extract the HTML content from the page
    html_content = driver.page_source

    # # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    law_classifier_div = soup.findAll('div', {"class": "lx_link"})

    # # Find all the <a> tags within the div
    # links = law_classifier_div.find_all('a')
    # # Extract the href links
    global s
    for i in law_classifier_div:
        link = re.search(r"lxOpenUrl\('([^']*)'\)", str(i)).group(1)
        link = "https://lex.uz/"+link+"\n"
        with open("links"+str(s)+".txt", "a") as file:
            file.write(link)
    s=s+1


Urls = []
with open("pages.txt", 'r') as file:
    Urls = file.readlines()

for url in Urls:
    writing_links(url)


# href_links = [link['href'] for link in links]

# # # Print the extracted href links
# for href in href_links:
#     print(href)

# print(links)

# Close the Firefox WebDriver
driver.quit()
