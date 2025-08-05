from selenium import webdriver
from src.app.Worker import Worker

class Window:
    
    def __init__(self):
        self.window = self.__create() # create a window
        self.__options()
        Worker()
    
    @staticmethod
    def __create():
        window = webdriver.Chrome()
        return window
    
    def __options(self):
        self.window.maximize_window()
        # more options
        
        
        