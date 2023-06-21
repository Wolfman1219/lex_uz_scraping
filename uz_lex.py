from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

def expand_folders(driver, folder_xpath):
    try:
        folders = driver.find_elements(By.XPATH,folder_xpath)
        for folder in folders:
            folder.click()
            expand_folders(driver, folder_xpath)
    except NoSuchElementException:
        return

def get_all_links(driver, links_xpath):
    links = driver.find_elements(By.XPATH,links_xpath)
    return [link.get_attribute("href") for link in links]

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
url = 'https://lex.uz/uz/klassifkator'
driver.get(url)

wait = WebDriverWait(driver, 10)

# Adjust the XPath selectors according to your web page structure
folder_xpath = '//a[contains(@class, "fldr")]'
links_xpath = '//a[contains(@target, "_blank")]'

try:
    wait.until(EC.presence_of_all_elements_located((By.XPATH, folder_xpath)))
    expand_folders(driver, folder_xpath)
    wait.until(EC.presence_of_all_elements_located((By.XPATH, links_xpath)))
    all_links = get_all_links(driver, links_xpath)
    print(all_links)
except TimeoutException:
    print("Timeout: Could not find element(s) within the specified time.")
finally:
    driver.quit()