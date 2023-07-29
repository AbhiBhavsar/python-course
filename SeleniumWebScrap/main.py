from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Service
driver_path = "./chDriver/chromedriver.exe"
brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
option = webdriver.ChromeOptions()
option.binary_location = brave_path
service = Service(executable_path=driver_path)
browser = webdriver.Chrome(service=service, options=option)
browser.get("https://www.google.com")