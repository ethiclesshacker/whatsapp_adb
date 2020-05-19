from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver.exe")

driver.get("http://web.whatsapp.com")

input("Press any key after scanning QR code.")


def selectChat(name):
    search = driver.find_element_by_class_name("C28xL")
    search.click()
    searchBox = driver.switch_to.active_element
    searchBox.send_keys(name)
    searchBox.send_keys(Keys.ENTER)


def sendMultiMessage(message, count):
    textBox = driver.switch_to.active_element
    for _ in range(count):
        textBox.send_keys(message)
        textBox.send_keys(Keys.ENTER)


def newMessage():
    elem = driver.find_elements_by_class_name("rAUz7")
    elem[1].click()


name = "Random"
message = "Uth jao."
selectChat(name)
sendMultiMessage(message, 30)

driver.quit()
