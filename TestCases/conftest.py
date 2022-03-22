from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.fixture
def setup():
    print("Execution Started")
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    driver  = webdriver.Firefox(executable_path="C:\geckodriver.exe")
    print("Chrome browser launched")
    return driver

