from PageObject_Orange.UserManagement_Object import UserManagementObject
import pytest

class Test_001_UserManagement:
    url = "https://opensource-demo.orangehrmlive.com/"
    def test_addNewuser(self,setup):
        self.driver = setup
        self.driver.get(self.url)






