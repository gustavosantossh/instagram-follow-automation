from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.app.config.Config import Config

class FollowAccountInstagram:
    
    def __init__(self, window: WebDriver):
        self.__run(window)
        
    def __run(self, window: WebDriver):
        self.__follow_account(window)
    
    def __follow_account(self, window: WebDriver):
        window.get(f'https://www.instagram.com/{Config.USER_TO_FOLLOW}')
        
        wait = WebDriverWait(window, 100)
        
        follow_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Seguir')]")))
        follow_button.click()