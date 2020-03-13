from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from secrets import user_name, user_password
from selenium import webdriver
from random_strings import hashtags, comments
from urls import login_url, tags_url
import random


class Jarvis:
    def __init__(self, user, password):
        try:
            self.user_name = user
            self.user_password = password
            self.driver = webdriver.Chrome(
                executable_path='./chrome/chromedriver')
            self.actions = ActionChains(self.driver)
        except:
            pass

    def login(self):
        try:
            self.driver.get(login_url)
            sleep(2)

            self.driver.find_element_by_name('username').send_keys(user_name)
            sleep(1)

            self.driver.find_element_by_name(
                'password').send_keys(user_password)
            sleep(1)

            self.driver.find_element_by_xpath(
                '//button[@type="submit"]').click()
            sleep(5)

            self.driver.find_element_by_xpath(
                '//button[contains(text(), "Not Now")]').click()
            sleep(1)

        except:
            pass

    def explore(self, tags, comments, num_pics):
        try:
            self.driver.get(tags_url + random.choice(tags))
            sleep(2)

            self.driver.find_elements_by_class_name('_9AhH0')[0].click()
            sleep(2)

            for i in range(num_pics):
                try:
                    self.driver.find_elements_by_class_name('wpO6b')[0].click()
                    sleep(2)

                    self.driver.find_element_by_class_name('Ypffh').click()
                    self.driver.find_element_by_class_name('Ypffh').send_keys(
                        random.choice(comments) + Keys.ENTER)
                    sleep(5)

                    self.driver.find_element_by_link_text('Next').click()
                    sleep(2)
                except:
                    pass
        except:
            pass

    def show_love(self):
        print('love')

    def write_to_file(self, file_name, text):
        try:
            file = open(file_name, 'w')
            file.write(text)
            file.close()
        except:
            pass

    def read_from_file(self, read_file):
        try:
            file = open(read_file)
            for line in file:
                print(line)
            file.close()
        except:
            pass


jarvis = Jarvis(user_name, user_password)
jarvis.login()
jarvis.explore(hashtags, comments, 10)
