#  it's essencial that the user first pip install selenium on his system or on the source code editor such as visual code
#  afterwards download the latest geckodriver on github and unzip it on the root of your python folder
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time

class TwitterBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/login')
        time.sleep(5) #  I used a timer to load wait for the page to load before entering the login and password
        email = bot.find_element_by_name("session[username_or_email]")
        password = bot.find_element_by_name("session[password]")
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(5)

    def like_tweet(self,hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typeahead_click')
        time.sleep(3)
        for i in range(6):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(3)
            tweets = bot.find_elements_by_xpath('//div[@data-testid="tweet"]')
            for tweet in tweets:
                bot.find_element_by_xpath('//div[@data-testid="like"]').click()
                time.sleep(3)

bot = TwitterBot('','') # Enter here your username/e-mail and password like this: ('email@email.com','password')
bot.login()
bot.like_tweet('artificial intelligence') # Enter here the subject you want the bot to search for ('subject')
