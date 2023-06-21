from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import re
from random import randint
import uuid
from selenium.common.exceptions import NoSuchElementException

# Set the path to the Firefox driver executable
webdriver_path = 'geckodriver.exe'
binary_path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
# Set up the Firefox options
firefox_options = Options()
# firefox_options.add_argument('--headless')  
# Run Firefox in headless mode (without GUI)
firefox_options.binary_location = binary_path
firefox_options.add_argument('--no-sandbox')
# firefox_options.add_argument('--headless')

# Start the Firefox WebDriver
driver = webdriver.Firefox(service=Service(webdriver_path), options=firefox_options)
driver2 = webdriver.Firefox(service=Service(webdriver_path), options=firefox_options)

# Load the web page using Selenium

 # Replace with the URL of the web page you want to scrape

def get_text(url):
    filename = "texts\\"+str(uuid.uuid4())+".txt"
    driver2.get(url)
    div_element = driver2.find_element(By.XPATH,"//div[@class='docBody__container']")
    text = div_element.text
    with open(filename, "w", encoding="utf-8") as file:
        file.write(str(text))
    # driver2.quit()

# links = []

def writing_links(url):
    driver.get(url)
    s = 1
    while True:
        print(url+f"   page: {s} ")
        # Extract the HTML content from the page
        html_content = driver.page_source

        # # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        law_classifier_div = soup.findAll('a', {"class": "lx_link"})
        global links
        # # Extract the href links
        for i in law_classifier_div:
            match = re.search(r'href="([^"]+)"', str(i))
            if match:
                link = match.group(1)
                link = "https://lex.uz/"+link
                # links.append(link)
                try:
                    get_text(link)
                except:
                    print("excepted link: "+link)
        try:
            element = driver.find_element(By.XPATH,"//a[@id=\"ucFoundActsControl_LinkButton1\"]") 
            element = element.click()
            s = s+1
        except NoSuchElementException:
            break
    


for i in range(0,20):
    Urls = []
    with open(f"links/links{i}.txt", 'r') as file:
        Urls = file.readlines()

    for url in Urls:
        try:
            writing_links(url)
        except:
            continue



# href_links = [link['href'] for link in links]

# # # Print the extracted href links
# for href in href_links:
#     print(href)

# print(links)

# Close the Firefox WebDriver
driver2.quit()
driver.quit()