from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import csv



# Gets URLs from CSV file
def getUrls():
     urls = open("urls.csv", "r", encoding="utf-8")

     for url in urls.readlines():
          url = url.strip("\n")

          # Send the URLs to web driver
          webdriver_(url)




def webdriver_(url):
    webdriver_service = Service('YOUR PATH /chromedriver.exe') 
    chrome_options = Options()
    driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

    try:
        driver.get(url)
    except:
         print("Error at the get url")
         return

    # Initialize to get Product Info function
    productInfo = getProductInfo(driver)

    # Initialize to get Product Pictures function
    pictureUrls = getProductPictures(driver)

    # Initialize function that to create CSV file with extracted datas
    createCSV(productInfo,pictureUrls)







def getProductInfo(driver):

     productInfo = []

     # ProductName
     productName = driver.find_element(By.CLASS_NAME,"product_title")

     # Product Details
     productDetailTable = driver.find_element(By.CLASS_NAME,"row-hover")
     rows = productDetailTable.find_elements(By.TAG_NAME, "tr")
     for row in rows:
          columns = row.find_elements(By.TAG_NAME, "td")

          if len(columns) == 2:
               column_1 = row.find_element(By.CLASS_NAME, "column-1")
               column_2 = row.find_element(By.CLASS_NAME, "column-2")

               label = column_1.get_attribute("textContent")
               value = column_2.get_attribute("textContent")

               productInfo.append([productName,label,value])

        
     return productInfo





def getProductPictures(driver):
     pictureUrls = []
     slider = driver.find_element(By.CLASS_NAME,"woocommerce-product-gallery__wrapper")
     slide_images = slider.find_elements(By.CLASS_NAME,"woocommerce-product-gallery__image")

     for slide_image in slide_images:
          image = slide_image.find_element(By.TAG_NAME,"img")
          pictureUrls.append(image.get_attribute("src"))

     return pictureUrls




def createCSV(productInfo,pictureUrls):
     with open('rolex.csv', 'a', newline='', encoding='utf-8') as csvfile:
          writer = csv.writer(csvfile)
          writer.writerow([productInfo,pictureUrls])


     


if __name__ == "__main__":
     getUrls()






