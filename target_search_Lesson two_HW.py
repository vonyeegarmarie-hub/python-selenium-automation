from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver=webdriver.Chrome()
driver.maximize_window()
sleep(4)


driver.get('https://www.target.com')
sleep(5)

#click account button
driver.find_element(By.XPATH, "//*[@data-test='@web/AccountLink']").click()

#Sign in button from side
driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()

sleep(5)

#Verify
#expected = 'Sign in or create account'
#actual = driver.find_element(By.XPATH, "//h1[contains@class, 'styles_ndsHeading')]").text
driver.find_element(By.XPATH, "//*[(text()='Sign in or create account')]")
#sign in button shown
driver.find_element(By.ID, "login")

driver quit()
#