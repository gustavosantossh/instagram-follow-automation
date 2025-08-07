from selenium.webdriver.remote.webdriver import WebDriver
from src.app.services.Mail import Mail
from src.app.actions.CreateAccountInstagram import CreateAccountInstagram
from src.app.actions.FollowAccountInstagram import FollowAccountInstagram

class Worker:
    
    def __init__(self, window: WebDriver):
        self.__run(window)
        
    def __run(self, window):
        credential = Mail.createMailAccount()
        CreateAccountInstagram(window, credential)
        FollowAccountInstagram(window)
        
      