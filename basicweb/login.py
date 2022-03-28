from datetime import datetime

from selenium import webdriver
from unittest import TestCase

from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class ChromeDriverWindows(TestCase):
    def site_login(self):
        # Invalid Login case
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://premark-demo.bridge-teams.com/login")
        driver.find_element(By.ID, "input-1").send_keys("admin")
        driver.find_element(By.ID, "input-2").send_keys("fake")
        driver.find_element(By.XPATH, "//*[@id='__layout']/div/div/div[2]/div/div[1]/div[2]/div/div/div[2]/form/div["
                                      "2]/button").click()
        wait = WebDriverWait(driver, 10000)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'alert-danger')))
        error_message = driver.find_element(By.CLASS_NAME, 'alert-danger').text
        self.assertAlmostEqual(error_message, 'Uw inloggegevens zijn verkeerd. Probeer het opnieuw.')

        driver.find_element(By.ID, "input-1").clear()
        driver.find_element(By.ID, "input-1").send_keys("admin")
        driver.find_element(By.ID, "input-2").clear()
        driver.find_element(By.ID, "input-2").send_keys("password")
        #click on login
        driver.find_element(By.XPATH, "//*[@id='__layout']/div/div/div[2]/div/div[1]/div[2]/div/div/div[2]/form/div["
                                      "2]/button").click()

        layout_wrapper = '//*[@id="layout-wrapper"]/div/div/div/div/div[2]/div[1]/div/div/a'
        # Waiting for home page is loading
        Newelement = wait.until(EC.visibility_of_element_located((By.XPATH, layout_wrapper)))
        self.assertTrue(Newelement)
        # click on new notification button
        Newelement.click()
        # Waiting for loading thew new notification page
        bvElement = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="complaints"]/div/textarea')))
        #Fill the date
        datrePicker = '//*[@id="notification_date"]/div/div'
        driver.find_element(By.XPATH, datrePicker).click()
        dateCollection = driver.find_elements(By.CLASS_NAME, 'mx-date-row')
        today = datetime.today().strftime('%Y-%m-%d')
        for eachField in dateCollection:
            for DateField in eachField.find_elements(By.TAG_NAME, 'td'):
                if (DateField.get_attribute("title") == today):
                    DateField.click()
                    break
        # Fill property User
        driver.find_element(By.ID, 'property_user').click()
        driver.find_element(By.XPATH, '//*[@id="property_user"]/div/div/div/div[2]/input').send_keys('br')
        wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="property_user"]/div/div/div/div[3]/ul/li[1]/span')))
        propert = driver.find_element(By.XPATH, '//*[@id="property_user"]/div/div/div/div[3]/ul/li[1]/span/span')
        if propert.text == 'Bridge Global':
            propert.click()

        driver.find_element(By.XPATH, '//*[@id="property_management"]/div/div/div/div[2]/input').click()

        wait.until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="property_management"]/div/div/div[1]/div[3]/ul/li[1]/span/span')))
        driver.find_element(By.XPATH, '//*[@id="property_management"]/div/div/div[1]/div[3]/ul/li[1]/span/span').click()

        driver.find_element(By.XPATH, '//*[@id="reporter_name"]/div/input').send_keys('tester')

        driver.find_element(By.XPATH, '//*[@id="location"]/div/input').send_keys('kochi')

        driver.find_element(By.XPATH, '//*[@id="type_of_complaint"]/div/div/div/div[2]/input').click()
        driver.find_element(By.XPATH, '//*[@id="type_of_complaint"]/div/div/div/div[3]/ul/li[1]/span').click()

        driver.find_element(By.XPATH, '//*[@id="complaints"]/div/textarea').send_keys('test complaints....')

        self.waitForElementToVisible(driver, '//*[@id="term"]/div/div/div/div[2]/input')
        driver.find_element(By.XPATH, '//*[@id="term"]/div/div/div[1]/div[3]/ul/li[1]').click()
        self.waitForElementToVisible(driver, '//*[@id="maintenance"]/div/div/div[1]/div[2]/input')
        driver.find_element(By.XPATH, '//*[@id="maintenance"]/div/div/div[1]/div[3]/ul/li[1]/span').click()
        self.waitForElementToVisible(driver,
                                                    '//*[@id="layout-wrapper"]/div/div/div/div/div[2]/div/div/form/div/div/div/div[16]/div/button')










        wait.until(EC.visibility_of_element_located((By.XPATH, "adsgrthyjkuii")))

    def waitForElementToVisible(self, driver, xpath):
        header_element = driver.find_element(By.TAG_NAME, 'header')
        additional_header_elem = driver.find_element(By.XPATH, '//*[@id="page-topbar"]/div[2]')
        elem = driver.find_element(By.XPATH, xpath)
        scroll_y_by = (elem.location_once_scrolled_into_view['y'] - (
                header_element.size['height'] + additional_header_elem.size['height']))
        driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
        while True:
            try:
                current_element = WebDriverWait(driver, 455).until(EC.presence_of_element_located((By.XPATH, xpath)))
                current_element.click()
                break
            except ElementClickInterceptedException:
                continue
        return elem

obj = ChromeDriverWindows()
obj.site_login()
