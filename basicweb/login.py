from selenium import webdriver
from unittest import TestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class chromedriverwindows(TestCase):
    def site_login(self):
        # Invalid Login case
        driver = webdriver.Chrome(executable_path="C:\\Users\\bridge\\workspace_python\\drivers\\chromedriver.exe")
        driver.get("https://premark-demo.bridge-teams.com/login")
        driver.find_element(By.ID, "input-1").send_keys("admin")
        driver.find_element(By.ID, "input-2").send_keys("fake")
        driver.find_element(By.XPATH, "//*[@id='__layout']/div/div/div[2]/div/div[1]/div[2]/div/div/div[2]/form/div["
                                      "2]/button").click()
        WebDriverWait(driver=driver, timeout=1000).until(
            lambda x: x.execute_script("return document.readyState === 'complete'")
        )
        wait = WebDriverWait(driver, 10000)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'alert-danger')))
        errorMssg = driver.find_element(By.CLASS_NAME, 'alert-danger').text
        self.assertAlmostEqual(errorMssg, 'Uw inloggegevens zijn verkeerd. Probeer het opnieuw.')

        driver.find_element(By.ID, "input-1").clear()
        driver.find_element(By.ID, "input-1").send_keys("admin")
        driver.find_element(By.ID, "input-2").clear()
        driver.find_element(By.ID, "input-2").send_keys("password")
        driver.find_element(By.XPATH, "//*[@id='__layout']/div/div/div[2]/div/div[1]/div[2]/div/div/div[2]/form/div["
                                      "2]/button").click()
        newButton = '//*[@id="layout-wrapper"]/div/div/div/div/div[2]/div[1]/div/div/a'
        Newelement = wait.until(EC.visibility_of_element_located((By.XPATH, newButton)))
        self.assertTrue(Newelement)
        Newelement.click()
        bvElement = wait.until(EC.visibility_of_element_located((By.ID, "__BVID__151")))
        bvElement.send_keys("asdf")


        #wait.until(EC.visibility_of_element_located((By.XPATH, "adsgrthyjkuii")))


ff = chromedriverwindows()
ff.site_login()