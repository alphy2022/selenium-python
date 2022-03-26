from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\bridge\\workspace_python\\drivers\\chromedriver.exe")

driver.implicitly_wait(10)

driver.maximize_window()

driver.get("https://premark-demo.bridge-teams.com/login")

driver.find_element_by_id("input-1").send_keys("admin")

driver.find_element_by_id("input-2").send_keys("password")

driver.find_element_by_xpath("//button[@class='btn w-sm btn-primary']").click()

driver.implicitly_wait(20)

driver.find_element_by_xpath("//a[@href='/meldingen']").click()

driver.implicitly_wait(20)

driver.find_element_by_xpath("//a[@href='/meldingen/edit/59']").click()

driver.execute_script("window.scrollTo(500, window.scrollY + 2500)")


#driver.implicitly_wait(20)

#driver.find_element_by_xpath("//a[@class='btn btn-primary']").click()