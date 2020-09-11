from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep
driver = webdriver.Chrome(ChromeDriverManager().install())

#go to site
driver.get("https://play.typeracer.com/")
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/button[3]").click()
#start game
sleep(5)
driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td/a").click()
#get text
sleep(5)
prima = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[1]")
sleep(3)
restu = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[2]")
sleep(3)
tot = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[3]")

baga = prima.text + restu.text +" " + tot.text
sleep(5)
for word in baga:
	driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/input").send_keys(word)