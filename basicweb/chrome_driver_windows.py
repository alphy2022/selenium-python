from selenium import webdriver
class chromedriverwindows():
    def testMethod(self):
        driver=webdriver.Chrome(executable_path="C:\\Users\\bridge\\workspace_python\\drivers\\chromedriver.exe")
        driver.get("http://www.google.com")
ff=chromedriverwindows()
ff.testMethod()


