from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome(executable_path='C:\\Users\\bridge\\workspace_python\\drivers\\chromedriver.exe')

driver.implicitly_wait(10)

driver.maximize_window()

driver.get("https://premark-demo.bridge-teams.com/login")
wait = WebDriverWait(driver, 10000)

driver.find_element(By.ID, "input-1").send_keys("admin")
driver.find_element(By.ID, "input-2").send_keys("password")
driver.find_element(By.XPATH, "//*[@id='__layout']/div/div/div[2]/div/div[1]/div[2]/div/div/div[2]/form/div["
                                      "2]/button").click()

wait.until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="layout-wrapper"]/div/div/div/div/div[2]/div[1]/div/div/a')))
element_to_hover_over = driver.find_element(By.XPATH, '//*[@id="topnav-menu-content"]/ul/li[3]')
ActionChains(driver).move_to_element(element_to_hover_over).perform()
driver.find_element(By.XPATH, '//*[@id="topnav-menu-content"]/ul/li[3]/div/a[2]').click()