from PageObject_Orange.UserManagement_Object import UserManagementObject
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Test_001_UserManagement:
    url = "https://opensource-demo.orangehrmlive.com/"
    UserName = "Admin"
    Password = "admin123"
    def test_addNewuser(self, setup):
        self.driver = setup
        print(self.driver)
        self.driver.get(self.url)
        self.driver.maximize_window()
        print("Middle of Execution")
        self.UM = UserManagementObject(self.driver)
        print(self.UM.LoginuserName_id)

        # self.driver.find_element_by_id(self.UM.LoginuserName_id).sendkey(self.UserName)
        self.UM.UserName(self.UserName)
        print("Execution Ends Here.................................")


