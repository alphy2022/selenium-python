from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class geckodriverwindows():
    def premark_login(self):
        driver=webdriver.Firefox(executable_path="C:\\Users\\bridge\\workspace_python\\drivers\\geckodriver.exe")
        wait = WebDriverWait(driver, 10000)
        driver.get("https://premark-demo.bridge-teams.com/login")
        driver.find_element(By.ID,"input-1").send_keys("admin")
        driver.find_element(By.ID,"input-2").send_keys("password")
        driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div/div[2]/div/div[1]/div[2]/div/div/div[2]/form/div[2]/button').click()
        #wrongButton=
        newButton='//*[@id="layout-wrapper"]/div/div/div/div/div[2]/div[1]/div/div/a'
        newElement = wait.until(EC.visibility_of_element_located((By.XPATH, newButton)))
        newElement.click()
        bvElement = wait.until(EC.visibility_of_element_located((By.ID, "__BVID__151")))
        bvElement.send_keys("asdf")
        assertTrue(self.is_element_present(By.ID, "footer"))
        wait.until(EC.visibility_of_element_located((By.XPATH, "adsgrthyjkuii")))

ff = geckodriverwindows()
ff.premark_login()
