from selenium import webdriver
import math
import time

try:
    link = " http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_xpath("/html/body/form/div/div/button")
    button.click()
    time.sleep(1)
    alert = browser.switch_to.alert
    alert_text = alert.text
    alert.accept()
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    print(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    button = browser.find_element_by_xpath("/html/body/form/div/div/button")
    button.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    alert.accept()
    print(alert_text.split()[-1])
    # time.sleep(2)
    window_name = "https://stepik.org/lesson/184253/step/4?unit=158843"
    browser.switch_to.window(window_name)
    
    # link2 = "https://stepik.org/lesson/184253/step/4?unit=158843"
    # browser = webdriver.Chrome()
    # browser.get(link2)
    # input2 = browser.find_element_by_id("answer")
    # input2.send_keys(alert_text)


    # alert_text.split(': ')[-1]
    # print(alert_text.split()[-1])

finally:
    time.sleep(10)
    browser.quit()