# from selenium import webdriver
# import time
#
# browser = webdriver.Chrome()
# #browser.execute_script("alert('Robots at work');")
# prompt = browser.switch_to.alert
# prompt.send_keys("OKI DOKI lolololadasdasdasd")
# time.sleep(2)
# prompt.accept()

from selenium import webdriver


browser = webdriver.Chrome()
link='file:///E:stepik/hol.html'
browser.get(link)
alert = browser.switch_to.alert()
alert.accept()

alert = browser.switch_to.alert()