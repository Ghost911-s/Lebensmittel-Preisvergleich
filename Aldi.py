from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from selenium.webdriver import chrome

PATH = "/Users/maxbl/OneDrive/Desktop/Coding/chromedriver.exe"

driver = webdriver.Chrome(PATH)
#load the website
driver.get(r"https://www.aldi-nord.de/")
time.sleep(5)
#click the "Prospekte"
driver.find_element_by_xpath("/html/body/header/div/nav/div[1]/div[2]/div[1]/div/div[1]/ul/li[3]/a/span[2]").click()
time.sleep(3)
#get to the current Prospekt
driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/div[1]/div[1]/div/div[2]/a").click()


def pick_a_product():
    print("Hello, which product would you like to choose ? ")
    print("")
    #Wie machen wir es bzgl. Tippfehlern bei der Produkt suche ? 
    #und wie machen wir es bzgl. Cola => Coca Cola, Pepsi Cola etc

    choosen_product = input()

    print("You choose ", choosen_product)
    
    return choosen_product

#product= pick_a_product()


def enter_website():
    driver.get(r"https://www.aldi-nord.de/")
    search_bar = driver.find_element_by_name("q")
    search_bar.send_keys(product)
    search_bar.send_keys(Keys.RETURN)

#enter_website()
