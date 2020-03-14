# Jarvis

## Overview:

Jarvis is a friendly bot that likes users' ig posts and leaves friendly comments on them.<br/>
He was created in Python3 using the Selenium Webdriver API.

Jarvis has three ways of interacting with your account:

- Liking and leaving a random comment on posts with a randomly selected hashtag.
- Liking and leaving a random comment on posts from the explore page.
- Liking posts from users that you follow.<br/>
  <br/>
  (selection of hashtags and comments are provided by the user.)

Jarvis can also be easily reprogrammed to perform other tasks on your account.

## Set up:

To use Jarvis, you will need to fork and or clone this repo, and install the following tools:

- Selenium Python package<br/>
  `pip install selenium`<br/>
  This will allow acces to the Selenium Webdriver API for automated interactions with the DOM.

- ChromeDriver<br/>
  http://chromedriver.chromium.org/<br/>
  This will allow automated navigation capabilities in the Google Chrome web browser.

Remember to change the executable path for `self.driver` in the Jarvis `__init__` method to be the path of your own ChromeDrive executable file.

## Jarvis API:

### `__init__(self, user: str, password: str)`

Pre conditions:

- User has successfully installed Selenium and ChromeDriver

Post conditions:<br/>
A Jarvis instance will have the following properties:

- `self.user_name`
  User name provided.

- `self.user_password`
  Password provided.

- `self.driver`
  Selenium Webdriver instance that will be used for DOM interaction.

- `self.actions`
  selenium.webdriver.common.action_chains instance for additional complex DOM related functionalities (such as drag and drop.)

### Syntax

`jarvis_instance = Jarvis('username', 'password')`

---

### `login(self)`

Pre conditions:

- Active ig account.
- Correct user name and password combination provided.

Post conditions:

- Logs in to the account provided. Execution terminates once home page is reached.

### Syntax

`jarvis_instance.login()`

---

### `explore(self, tags: list/str, comments: list, posts: int)`

Pre conditions:

- Jarvis has successfully logged in to the provided account.
- `tags` is a list of strings with length >= 1 representing possible hashtags Jarvis can visit.
  `tags` can also be the string `'assorted'` to tell Jarvis to visit the explore page.
- `comments` is a list of strings with length >= 1 representing possible comments Jarvis can make on a particular post.
- `posts` is an integer >= 0 that tells Jarvis how many posts to go through.

Post conditions:

- Jarvis will go through the specified amount of posts, from either the explore page or hashtags page,
  liking and leaving a randomly selected comment on each one.

### Syntax

`jarvis_instance.explore(['sports', 'nature', 'photography'], ['nice!', 'awesome!', 'wow'], 50)` or ...
`jarvis_instance.explore('assorted', ['nice!', 'awesome!', 'wow'], 50)`

---

### `show_love(self, posts: int)`

Pre conditions:

- Jarvis has successfully logged in to the provided account.
- `posts` is an integer >= 0 that tells Jarvis how many posts to go through.

Post conditions:

- Jarvis will go through the specified amount of posts in your feed liking approximately 60% of them.
  The rest will be skipped as Jarvis scrolls past them.

### Syntax

`jarvis_instance.show_love(50)`

---
