from webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import smtplib
import time
import random
import logging

class Bot:
    def __init__(self, start_page_url):
        self.webdriver = WebDriver()
        self.start_page_url = start_page_url

    def go_to_start_page(self):
        self.webdriver.open_url(self.start_page_url)

    def refresh(self):
        self.webdriver.refresh()

    def go_to_festival_page(self, festival_name):
        self.webdriver.fill_in_input_field("/html/body/div[1]/div[1]/section/div[2]/div/div/div[1]/label/div[2]/input",
                                           festival_name)
        time.sleep(1)
        self.select_item_by_x_path('//*[@id="site-search-item-0"]')

    def quit(self):
        self.webdriver.quit()

    def is_on_start_page(self):
        return self.webdriver.get_current_url() == self.start_page_url

    def select_item(self, item_name):
        item = self.webdriver.find_element_by_x_path(f'//*[text()="{item_name}"]')
        return self.webdriver.click_on_element(item)

    def select_item_by_x_path(self, item_x_path):
        item = self.webdriver.find_element_by_x_path(item_x_path)
        #print(item)
        return self.webdriver.click_on_element(item)

    def go_to_ticket_page(self, otherCategory, ticketName):
        if otherCategory == "":
            self.select_item_by_x_path(f'//*[text()="{ticketName}"]')
        else:
            self.select_item(otherCategory)
            time.sleep(1)
            self.select_item_by_x_path(f'//*[text()="{ticketName}"]')

    def find_available(self):
        try:
            self.webdriver.find_element_by_x_path('//*[text()="Jelenleg nincs elérhető jegy"]')
        except (NoSuchElementException, TimeoutException):
            '''try:
                if self.webdriver.find_element_by_x_path('//*[text()="Valami hiba történt... kérjük, lépj velünk kapcsolatba, ha a hiba továbbra is fennáll."]'):
                    logging.error("Page error, sleep 300")
                    time.sleep(300)
                    return False
            except:
                return True'''
            return True
        return False

    def jump_to_ticket_page(self):
        self.go_to_start_page()
        time.sleep(0.3)
        self.select_item_by_x_path("/html/body/div[1]/div[2]/div[3]/div[1]/a[1]")
        time.sleep(0.3)
        self.go_to_ticket_page(otherCategory="", ticketName="Állójegy")
       # self.refresh()

    def refresher(self):
        random_decimal = random.randint(50000, 150000) / 10000
        time.sleep(random_decimal)
        self.jump_to_ticket_page()
        try:
            self.webdriver.find_element_by_x_path('//*[text()="Minden jegy"]')
            return True
        except (NoSuchElementException, TimeoutException):
            return False


    def reserve_ticket(self):
        self.select_item_by_x_path("/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/a[1]")
        time.sleep(0.355)
        self.select_item_by_x_path('//*[text()="Kosárba"]')

    def login(self):
        input("Hit Enter when logged in")
'''
        self.select_item("Bejelentkezés")
        time.sleep(1)


        # provide input string to the previously selected field:
        self.webdriver.fill_in_input_field('//*[id()="email"]', "kolozsvari.dl@gmail.com")

        self.select_item("Folytatás e-mailen keresztül")

        # read input string from console:
        code = input("Email code: ")

        self.webdriver.fill_in_input_field('//*[id()="one-time-code-input-1"]', code[0])
        self.webdriver.fill_in_input_field('//*[id()="one-time-code-input-2"]', code[1])
        self.webdriver.fill_in_input_field('//*[id()="one-time-code-input-3"]', code[2])
        self.webdriver.fill_in_input_field('//*[id()="one-time-code-input-4"]', code[3])
        self.webdriver.fill_in_input_field('//*[id()="one-time-code-input-5"]', code[4])
        self.webdriver.fill_in_input_field('//*[id()="one-time-code-input-6"]', code[5])

        self.select_item("Beküldés")
'''

