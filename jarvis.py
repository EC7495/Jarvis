from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from secrets import user_name, user_password
from selenium import webdriver
from random_strings import hashtags, comments
from urls import login_url, tags_url
from random import choice as pick


class Jarvis:
    def __init__(self, user, password):
        self.user_name = user
        self.user_password = password
        self.driver = webdriver.Chrome(
            executable_path='./chrome/chromedriver')
        self.actions = ActionChains(self.driver)

    # logs in to the account provided
    def login(self):
        try:
            self.driver.get(login_url)
            sleep(pick(range(2, 4)))

            self.driver.find_element_by_name(
                'username').send_keys(self.user_name)
            sleep(pick(range(1, 4)))

            self.driver.find_element_by_name(
                'password').send_keys(self.user_password)
            sleep(pick(range(1, 4)))

            self.driver.find_element_by_xpath(
                '//button[@type="submit"]').click()
            sleep(pick(range(4, 6)))

            try:
                self.driver.find_element_by_xpath(
                    '//button[contains(text(), "Not Now")]').click()
                sleep(pick(range(1, 4)))

            except:
                pass

        except:
            print('you are not welcomed here')

    # likes and comments on posts with randomly selected hashtag
    def explore(self, tags, comments, posts):
        try:
            if tags == 'assorted':
                self.driver.get('https://www.instagram.com/explore/')
            else:
                self.driver.get(tags_url + pick(tags))
            sleep(pick(range(2, 5)))

            self.driver.find_elements_by_class_name('_9AhH0')[0].click()
            sleep(pick(range(1, 4)))

            while(posts):
                self.driver.find_elements_by_class_name('wpO6b')[0].click()
                sleep(pick(range(1, 4)))

                try:
                    self.driver.find_element_by_class_name('Ypffh').click()
                    self.driver.find_element_by_class_name('Ypffh').send_keys(
                        pick(comments))
                    self.driver.find_element_by_xpath(
                        '//button[@type="submit"]').click()
                    sleep(pick(range(5, 7)))

                    self.driver.find_element_by_link_text('Next').click()
                    sleep(pick(range(3, 6)))

                except:
                    sleep(pick(range(1, 3)))
                    self.driver.find_element_by_link_text('Next').click()

                posts -= 1
        except:
            print('houston, we have a problem')

    # likes posts from users the provided account is following
    def show_love(self, posts):
        try:
            while(posts):
                # sleep(pick(range(2, 5)))
                like_buttons = self.driver.find_elements_by_class_name('wpO6b')
                for btn in like_buttons:
                    try:
                        svg = btn.find_element_by_tag_name('svg')
                        if svg.get_attribute('aria-label') == 'Like' and svg.get_attribute('height') == '24':
                            btn.click()
                            sleep(pick(range(2, 5)))

                    except:
                        pass

                self.driver.execute_script(
                    'window.scrollTo(0, document.body.scrollHeight / 1.7);')

                posts -= 1

        except:
            print('jarvis is not feeling lovely')

    # writes
    def write_to_file(self, file_name, text):
        try:
            file = open(file_name, 'w')
            file.write(text)
            file.close()

        except:
            print('no ink in this pen')

    # reads from specified file
    def read_from_file(self, read_file):
        try:
            file = open(read_file)
            for line in file:
                print(line)
            file.close()

        except:
            print('forgot my reading glasses')


jarvis = Jarvis(user_name, user_password)
jarvis.login()
# jarvis.show_love(10)
# jarvis.explore(hashtags, comments, 50)
# jarvis.explore('assorted', comments, 50)
