

class UserManagementObject:
    LoginuserName_id = "divUsername"
    LoginPassword_id= "divPassword"
    Loginbutton_id = "btnLogin"
    UserName_Um="UserName"
    UserRole_UM="UserRole"
    EmployeeName_UM="UserRole"

    def __init__(self,driver):
        self.driver = driver

    def UserName(self,UserName):
        self.driver.find_element_by_id(self.LoginuserName_id).sendkey(self.UserName)
