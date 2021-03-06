# Jarvis

## Overview:

Jarvis is a friendly bot that likes users' ig posts and leaves friendly comments on them.<br/>
He was created using Python3 and the Selenium Webdriver API.

Jarvis has various ways of interacting with your account:

- Following users from the explore page.
- Liking and leaving a random comment on posts from the explore page.
- Liking and leaving a random comment on posts with a randomly selected hashtag.
- Liking posts from all users that you follow.
- Liking posts from a particular user.
  <br/>
  (selection of hashtags and comments are provided by the user.)

Jarvis can also be easily reprogrammed to perform other tasks on your account.

## Demo:

![Jarvis demo](public/jarvis.gif)

## Set up:

To use Jarvis, you will need to fork and or clone this repo, and install the following tools:

- Selenium Python package<br/>
  `pip install selenium`<br/>
  This will allow acces to the Selenium Webdriver API for automated interactions with the DOM.

- ChromeDriver<br/>
  http://chromedriver.chromium.org/<br/>
  This will allow automated navigation capabilities in the Google Chrome web browser.

Remember to change the executable path for `self.driver` in the Jarvis `__init__` method to be the path of your own ChromeDriver executable file.

## Jarvis API:

### `__init__(self, user: str, password: str)`

Pre conditions:

- User has successfully installed Selenium and ChromeDriver

Post conditions:<br/>
A Jarvis instance will have the following properties:

- `self.user_name`<br/>
  User name provided.

- `self.user_password`<br/>
  Password provided.

- `self.driver`<br/>
  Selenium Webdriver instance that will be used for DOM interaction.
  <br/>
  <br/>
  <strong>Return value:</strong> `self`

### Syntax

`jarvis_instance = Jarvis('username', 'password')`

---

### `login(self)`

Pre conditions:

- User has an active ig account.
- User provided correct user name and password combination.

Post conditions:

- Logs in to the account provided. Execution terminates once home page is reached.
  <br/>
  <br/>
  <strong>Return value:</strong> `self`

### Syntax

`jarvis_instance.login()`

---

### `explore(self, tags: list, comments: list, posts: int, follow: bool)`

Pre conditions:

- Jarvis has successfully logged in to the provided account.
- `tags` (Optional - Default value: `[]`)<br/>
  A list of strings representing possible hashtags Jarvis can visit. If empty, Jarvis will navigate to explore page
- `comments` (Optional - Default value: `[]`)<br/>
  A list of strings representing possible comments Jarvis can make on a particular post.
  Jarvis will not comment if list of comments is empty.
- `posts` (Optional - Default value: `20`)<br/>
  An integer denoting how many posts Jarvis should go through.
- `follow` (Optional - Default value: `False`)<br/>
  A boolean (or any other truthy or falsy value) denoting whether Jarvis should follow users as he likes and comments on their post or not.

Post conditions:

- Jarvis will go through the specified amount of posts, from either the explore page or hashtags page and like every single post. 
- Jarvis will leave a randomly selected comment on approximately 75% of those posts, if comments are provided. There is also approximately a 60% chance that Jarvis will follow the user of that particular post if `follow` is set to `True`.
- As Jarvis goes through each post, he will collect the username of the person who made the post and save it in a file called `log.txt`. Jarvis will also make a note if a comment was made and if the user was followed.<br/>
  <br/>
  `log.txt` example:<br/>
  ![log.txt example](public/log.png)
  <br/>
  <br/>
  <strong>Return value:</strong> `self`

### Syntax

`jarvis_instance.explore()` or ...<br/>
`jarvis_instance.explore(['sports', 'nature', 'photography'], ['nice!', 'awesome!', 'wow'], 50, True)` or ...<br/>
`jarvis_instance.explore([], [], 50, True)` or ...<br/>
`jarvis_instance.explore(['photography'], [], 50, True)`

---

### `show_love(self, posts: int, user: str)`

Pre conditions:

- Jarvis has successfully logged in to the provided account.
- `posts` (Optional - Default value: `20`)<br/>
  An integer denoting how many posts in the feed Jarvis should go through.
- `user` (Optional - Default value: `None`)<br/>
  A string that denotes whether Jarvis should show love to all users in feed, or just the user provided. If a user is provided, Jarvis will navigate to that particular user's profile.

Post conditions:

- Jarvis will go through the specified amount of posts in your feed, liking approximately 60% of them.
  The rest will be skipped as Jarvis scrolls past them. If a user is provided, Jarvis will navigate to their profile and go through the specified amount of posts, liking all unliked posts he comes across.
  <br/>
  <br/>
  <strong>Return value:</strong> `self`

### Syntax

`jarvis_instance.show_love()` or ...<br/>
`jarvis_instance.show_love(50, 'your_bff_user_name')`

---

### `share(self, recipient: str, tags: list, posts: int)`

Pre conditions:

- Jarvis has successfully logged in to the provided account.
- `recipient`<br/>
  A string that denotes which user Jarvis should share posts with.
- `tags` (Optional - Default value: `[]`)<br/>
  A list of strings representing possible hashtags Jarvis can visit. If empty, Jarvis will navigate to explore page
- `posts` (Optional - Default value: `20`)<br/>
  An integer denoting how many posts Jarvis should go through.

Post conditions:

- Jarvis will go through the specified amount of posts, from either the explore page or hashtags page and share approximately 40% of the posts he comes across.

### Syntax

`jarvis_instance.share('my_bff', ['memes', 'funny'], 10)`

---

### `write_to_file(self, file_name: str, text: str)`

Post conditions:

- Jarvis will open the file provided in "append" mode and append the text provided. If the file provided exists, Jarvis will open and append to that same file. Otherwise, Jarvis will create a new file with the name provided.<br/>

Pre conditions:

- A file name was provided in valid format.
- The text provided is a string, or any other data type that can be written to a file.

Post conditions:

- Jarvis will open the file provided in "append" mode and append the text provided. If the file provided exists, Jarvis will open and append to that same file. Otherwise, Jarvis will create a new file with the name provided.<br/>
  <br/>
  This method can be used as a web scraper or as a means of keeping track of the users Jarvis follows and the comments he leaves. Most of the time, you will use this method in conjuction with the `explore` method to create some sort of `log.txt` file.
  <br/>
  <br/>
  <strong>Return value:</strong> `file_name`

### Syntax

`jarvis_instance.write_to_file("log.txt", "Jarvis will append this text.")`

---

### `read_from_file(self, file_name: str)`

Pre conditions:

- A file name was provided in valid format.
- The file provided already exists.

Post conditions:

- Jarvis will open the file provided in "read" mode and print its contents on the shell.<br/>
  <br/>
  This method can be used as a tool to retrieve information from `log.txt` or any other file.
  <br/>
  <br/>
  <strong>Return value:</strong> `file_name`

### Syntax

`jarvis_instance.read_from_file("log.txt")`

---
