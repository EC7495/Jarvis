from time import sleep, localtime
from selenium import webdriver
from urls import login_url, tags_url, explore_page_url, user_url
from random import choice, uniform


class Jarvis:
    def __init__(self, user, password):
        self.user_name = user
        self.user_password = password
        self.driver = webdriver.Chrome(
            executable_path='./chrome/chromedriver')

    # logs in to the account provided
    def login(self):
        try:
            self.driver.get(login_url)
            sleep(choice(range(2, 4)))

            self.driver.find_element_by_name(
                'username').send_keys(self.user_name)
            sleep(choice(range(2, 4)))

            self.driver.find_element_by_name(
                'password').send_keys(self.user_password)
            sleep(choice(range(2, 4)))

            self.driver.find_element_by_xpath(
                '//button[@type="submit"]').click()
            sleep(choice(range(4, 6)))

            try:
                self.driver.find_element_by_xpath(
                    '//button[contains(text(), "Not Now")]').click()
                sleep(choice(range(2, 4)))

            except:
                pass

        except:
            return('you are not welcomed here')

        return self

    # likes and comments on posts with randomly selected hashtag
    def explore(self, tags=[], comments=[], posts=20, follow=False):
        try:
            comments_on = True if len(comments) else False

            if len(tags):
                self.driver.get(tags_url + choice(tags))
            else:
                self.driver.get(explore_page_url)

            sleep(choice(range(2, 5)))

            self.driver.find_element_by_class_name('_9AhH0').click()
            sleep(choice(range(2, 4)))

            # self.write_to_file('log.txt', ('Date: %d/%d/%d' % (localtime()[1], localtime()[2], localtime()[0]) + '\n' +
            #                                'Start Run: %d:%d' % (localtime()[3], localtime()[4]) + '\n\n'))

            while(posts):
                try:
                    # user = self.driver.find_element_by_class_name(
                    #     'e1e1d').get_attribute('innerText')
                    # self.write_to_file('log.txt', '-' * 25 +
                    #                    '\nUser: ' + user + '\n')

                    if follow:
                        try:
                            follow_btn = self.driver.find_element_by_class_name(
                                'bY2yH').find_element_by_tag_name('button')
                            if follow_btn.get_attribute('innerText') == 'Follow' and uniform(0, 1) > 0.4:
                                # self.write_to_file('log.txt', 'Followed\n')
                                follow_btn.click()
                            sleep(choice(range(2, 4)))

                        except:
                            pass

                    like_btn = self.driver.find_elements_by_class_name(
                        'ltpMr')[0].find_element_by_class_name('wpO6b')

                    if like_btn.find_element_by_tag_name('svg').get_attribute('aria-label') == 'Like':
                        like_btn.click()

                    sleep(choice(range(2, 4)))

                    if comments_on and uniform(0, 1) > 0.25:
                        comment = choice(comments)
                        # self.write_to_file(
                        #     'log.txt', 'Comment: ' + comment + '\n')

                        self.driver.find_element_by_class_name('Ypffh').click()
                        self.driver.find_element_by_class_name(
                            'Ypffh').send_keys(comment)
                        sleep(choice(range(2, 4)))

                        self.driver.find_element_by_xpath(
                            '//button[@type="submit"]').click()
                        sleep(choice(range(5, 7)))

                    self.driver.find_element_by_link_text('Next').click()
                    sleep(choice(range(3, 6)))

                except:
                    self.driver.find_element_by_link_text('Next').click()
                    sleep(choice(range(2, 4)))

                # self.write_to_file('log.txt', '-' * 25 + '\n\n')

                posts -= 1
        except:
            return('houston, we have a problem')

        # self.write_to_file('log.txt', 'End Run: %d:%d' %
        #                    (localtime()[3], localtime()[4]) + '\n\n' + '*' * 40 + '\n\n')
        self.driver.find_elements_by_class_name('wpO6b')[-1].click()

        return self

    # likes posts from users the provided account is following
    def show_love(self, posts=20, user=None):
        try:
            if user:
                self.driver.get(user_url + user)
                sleep(choice(range(2, 5)))

                self.driver.find_element_by_class_name('_9AhH0').click()
                sleep(choice(range(2, 4)))

                while(posts):
                    try:
                        like_btn = self.driver.find_element_by_xpath(
                            '/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button')
                        if like_btn.find_element_by_tag_name('svg').get_attribute('aria-label') == 'Like':
                            like_btn.click()
                        sleep(choice(range(2, 4)))

                        self.driver.find_element_by_link_text('Next').click()
                        sleep(choice(range(3, 6)))

                    except:
                        self.driver.find_element_by_link_text('Next').click()
                        sleep(choice(range(3, 6)))

            else:
                while(posts):
                    like_buttons = self.driver.find_elements_by_class_name(
                        'wpO6b')
                    for btn in like_buttons:
                        try:
                            svg = btn.find_element_by_tag_name('svg')
                            if svg.get_attribute('aria-label') == 'Like' and svg.get_attribute('height') == '24':
                                btn.click()
                                sleep(choice(range(2, 5)))

                        except:
                            pass

                    self.driver.execute_script(
                        'window.scrollTo(0, document.body.scrollHeight / 1.5);')

                    posts -= 1

        except:
            return('jarvis is not feeling lovely')

        return self

    def share(self, recipient, tags=[], posts=20):
        try:
            if len(tags):
                self.driver.get(tags_url + choice(tags))
            else:
                self.driver.get(explore_page_url)

            sleep(choice(range(2, 5)))

            self.driver.find_element_by_class_name('_9AhH0').click()
            sleep(choice(range(2, 4)))

            while(posts):
                try:
                    if uniform(0, 1) > 0.6:
                        self.driver.find_element_by_xpath(
                            '/html/body/div[4]/div[2]/div/article/div[2]/section[1]/button').click()
                        sleep(choice(range(2, 4)))

                        self.driver.find_element_by_xpath(
                            '//div[contains(text(), "Share to Direct")]').click()
                        sleep(choice(range(2, 4)))

                        self.driver.find_element_by_name(
                            'queryBox').send_keys(recipient)
                        sleep(choice(range(2, 4)))

                        self.driver.find_element_by_class_name(
                            'glyphsSpriteCircle__outline__24__grey_2').click()
                        sleep(choice(range(2, 4)))

                        self.driver.find_element_by_xpath(
                            '//button[contains(text(), "Send")]').click()
                        sleep(choice(range(2, 4)))

                    self.driver.find_element_by_link_text('Next').click()
                    sleep(choice(range(3, 6)))

                except:
                    self.driver.find_element_by_link_text('Next').click()
                    sleep(choice(range(3, 6)))

        except:
            return('jarvis is being greedy')

    # writes
    def write_to_file(self, file_name, text):
        try:
            file = open(file_name, 'a')
            file.write(text)
            file.close()

        except:
            return('no ink in this pen')

        return file

    # reads from specified file
    def read_from_file(self, file_name):
        try:
            file = open(file_name, 'r')
            for line in file:
                print(line)
            file.close()

        except:
            return('forgot my reading glasses')

        return file
