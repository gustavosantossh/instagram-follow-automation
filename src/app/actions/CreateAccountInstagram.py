from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
import time
import random

class CreateAccountInstagram:
    
    def __init__(self, window: WebDriver):
        self.run(window)
    
    @classmethod
    def run(self, window: WebDriver):
        CreateAccountInstagram.create_account(window)
    
    @classmethod
    def create_account(self, window: WebDriver):
        window.get('https://www.instagram.com/')
        
        wait = WebDriverWait(window, 100)
        
        create_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(@href, '/accounts/emailsignup/')]")))
        create_button.click()
        
        email_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name = 'emailOrPhone']")))
        email_input.clear()
        email_input.send_keys("kerrine778s43timated@somoj.com")
        
        password_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name = 'password']")))
        password_input.clear()
        password_input.send_keys("teste1234")
        
        fullName_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name = 'fullName']")))
        fullName_input.clear()
        fullName_input.send_keys("gfjhsffsd fsdf")
        
        username_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name = 'username']")))
        username_input.clear()
        username_input.send_keys("Admin_username_aaabbcc546443")
        
        wait.until(lambda driver: driver.find_element(By.XPATH, "//button[@type = 'submit']").is_enabled())
        
        register_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type = 'submit']")))
        window.execute_script('arguments[0].scrollIntoView(true);', register_button)
        register_button.click()
        
        # choose date of birth
        
        select_month = wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@title='Mês:']")))
        
        dropdown_select_month = Select(select_month)
        dropdown_select_month.select_by_value(str(random.randint(1,12)))
        
        select_day = wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@title='Dia:']")))
        
        dropdown_select_day = Select(select_day)
        dropdown_select_day.select_by_value(str(random.randint(1,31)))
        
        select_year = wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@title='Ano:']")))
        
        dropdown_select_year = Select(select_year)
        dropdown_select_year.select_by_value(str(random.randint(1965,2005)))
        
        wait.until(lambda driver: driver.find_element(By.XPATH, "//button[contains(text(), 'Avançar')]").is_enabled())
        
        next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Avançar')]")))
        next_button.click()
        
        time.sleep(25)
        
        