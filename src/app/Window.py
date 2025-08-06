from selenium import webdriver
from src.app.Worker import Worker

class Window:
    
    def __init__(self):
        self.window = self.__create() # create a window
        self.__window_options()
        Worker(self.window)
    
    @staticmethod
    def __create():
        options = webdriver.ChromeOptions()
        options.add_argument('--incognito')
        # options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        window = webdriver.Chrome(options=options)
        return window
    
    def __window_options(self):
        self.window.maximize_window()
        # more options
        
        
        