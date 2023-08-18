from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
import pywinauto


f = open("questions.txt", encoding="utf8")
text = f.read()
splited = text.split("--")


op = Options()
op.binary_location = "C:/Program Files/Mozilla Firefox/firefox.exe"

driver = webdriver.Firefox(executable_path='C:/Users/Asus/Downloads/geckodriver.exe',options=op)
driver.get("https://www.google.com/search?q=holistic+seo&oq=holistic+seo&aqs=chrome..69i64j69i58j69i65l4j69i60l2.5089j0j7&sourceid=chrome&ie=UTF-8#lpqa=a,,d,1")

gmailInput = driver.find_element(By.CLASS_NAME, "whsOnd")
gmailInput.send_keys("searchenginerankingjoy@gmail.com")
gmailInput.send_keys(Keys.ENTER)
time.sleep(2)
passInput = driver.find_element(By.CLASS_NAME, "whsOnd")
time.sleep(2)
passInput.send_keys("beratkoc")
passInput.send_keys(Keys.ENTER)

index = 0

for x in splited:
    index += 1

    rd = random.randrange(4, 15)
    print(index,rd,x)
    time.sleep(rd)
    
    pywinauto.mouse.click(button='left', coords=(379, 423))
    time.sleep(rd)
    pywinauto.keyboard.send_keys(x,with_spaces=True)

    pywinauto.mouse.click(button="left", coords=(612, 589))
    time.sleep(2)
    pywinauto.mouse.click(button="left", coords=(680, 415))
    time.sleep(2)
    pywinauto.mouse.click(button="left", coords=(978, 148))


