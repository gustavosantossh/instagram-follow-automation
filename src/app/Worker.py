from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.app.actions.CreateAccountInstagram import CreateAccountInstagram

class Worker:
    
    def __init__(self, window: WebDriver):
        CreateAccountInstagram(window)
      
       
