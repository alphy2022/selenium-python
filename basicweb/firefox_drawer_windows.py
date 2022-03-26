from selenium import webdriver
#initiate ff browser command
#open provided url
#driver.get("https://www.google.com")

from selenium import webdriver


class RunFFTests():
    def testMethod(self):
        driver = webdriver.Firefox(executable_path=r"C:\Users\bridge\workspace_python\drivers\geckodriver.exe")
        driver.get("http://www.gmail.com")

ff = RunFFTests()
ff.testMethod()
# initiate ff browser command

# open provided url



