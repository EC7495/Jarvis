from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from secrets import user_name, user_password
from selenium import webdriver

login_url = 'https://www.instagram.com/accounts/login/?source=auth_switcher'
tags_url = 'https://www.instagram.com/explore/tags/'
hashtags = ['leagueoflenses', 'nature']


class Jarvis:
    def __init__(self, user, password):
        self.user_name = user
        self.user_password = password
        self.driver = webdriver.Chrome(executable_path='./chrome/chromedriver')
        self.actions = ActionChains(self.driver)

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

    def explore(self, tag):

        self.driver.get(tags_url + tag)
        sleep(2)

        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]').click()
        sleep(2)

        for i in range(10):
            # self.actions.double_click(self.driver.find_element_by_xpath(
            #     '/html/body/div[4]/div[2]/div/article/div[1]/div/div/div[1]/div[2]')).perform()
            self.driver.find_element_by_xpath(
                '/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button').click()
            sleep(2)

            self.driver.find_element_by_link_text('Next').click()
            sleep(2)

    def show_love(self):
        print('love')

    def write_to_file(self, file_name, text):
        file = open(file_name, 'w')
        file.write(text)
        file.close()

    def read_from_file(self, read_file):
        file = open(read_file)
        for line in file:
            print(line)
        file.close()


jarvis = Jarvis(user_name, user_password)
jarvis.login()
jarvis.explore(hashtags[0])
