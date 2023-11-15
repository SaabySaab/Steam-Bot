from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


from config import keys

options = Options()
options.add_experimental_option("detach", True)
options.add_argument('disable-infobars')
options.add_argument('start-maximized')

def order(k):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                              options=options)
    driver.get(k['product_url'])

    driver.find_element("xpath",'//*[@id="modal-root"]/div/div/div/div/div/section/div[2]/div/button').click()


if __name__ == '__main__':
    order(keys)