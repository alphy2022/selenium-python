from datetime import datetime
import time

from selenium import webdriver
from unittest import TestCase

from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class ChromeDriverWindows(TestCase):
    def siteMethod(self):
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
        # click on login
        driver.find_element(By.XPATH, "//*[@id='__layout']/div/div/div[2]/div/div[1]/div[2]/div/div/div[2]/form/div["
                                      "2]/button").click()
        # xpath of new button
        layout_wrapper = '//*[@id="layout-wrapper"]/div/div/div/div/div[2]/div[1]/div/div/a'
        # Waiting for home page is loading
        Newelement = wait.until(EC.visibility_of_element_located((By.XPATH, layout_wrapper)))
        # verify the button
        self.assertTrue(Newelement)
        # click on new notification button
        Newelement.click()
        # Waiting for loading thew new notification page
        bvElement = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="complaints"]/div/textarea')))
        # Fill the date
        datePicker = '//*[@id="notification_date"]/div/div'
        driver.find_element(By.XPATH, datePicker).click()
        dateCollection = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'mx-table-date')))
        today = datetime.today().strftime('%Y-%m-%d')
        dateCollection.find_element(By.CSS_SELECTOR, 'td[title^="{}"]'.format(today)).click()

        # Fill property User
        driver.find_element(By.ID, 'property_user').click()
        driver.find_element(By.XPATH, '//*[@id="property_user"]/div/div/div/div[2]/input').send_keys('br')
        wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="property_user"]/div/div/div/div[3]/ul/li[1]/span')))
        property = driver.find_element(By.XPATH, '//*[@id="property_user"]/div/div/div/div[3]/ul/li[1]/span/span')
        if property.text == 'Bridge Global':
            property.click()
        # fill property management
        driver.find_element(By.XPATH, '//*[@id="property_management"]/div/div/div/div[2]/input').click()
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="property_management"]/div/div/div[1]/div[3]/ul/li[1]/span/span')))
        driver.find_element(By.XPATH, '//*[@id="property_management"]/div/div/div[1]/div[3]/ul/li[1]/span/span').click()
        # fill contact person detail
        driver.find_element(By.XPATH, '//*[@id="reporter_name"]/div/input').send_keys('tester')
        # fill location
        driver.find_element(By.XPATH, '//*[@id="location"]/div/input').send_keys('kochi')
        # fill type of complaint
        driver.find_element(By.XPATH, '//*[@id="type_of_complaint"]/div/div/div/div[2]/input').click()
        driver.find_element(By.XPATH, '//*[@id="type_of_complaint"]/div/div/div/div[3]/ul/li[1]/span').click()
        # fill complaint details
        driver.find_element(By.XPATH, '//*[@id="complaints"]/div/textarea').send_keys('test complaints....')

        self.waitThenScrollAndClick(driver, '//*[@id="term"]/div/div/div/div[2]/input')
        driver.find_element(By.XPATH, '//*[@id="term"]/div/div/div[1]/div[3]/ul/li[1]').click()
        self.waitThenScrollAndClick(driver, '//*[@id="maintenance"]/div/div/div[1]/div[2]/input')
        driver.find_element(By.XPATH, '//*[@id="maintenance"]/div/div/div[1]/div[3]/ul/li[1]/span').click()
        self.waitThenScrollAndClick(driver,
                                    '//*[@id="layout-wrapper"]/div/div/div/div/div[2]/div/div/form/div/div/div/div[16]/div/button')

        wait.until(EC.presence_of_element_located((By.TAG_NAME, 'table')))
        # home page
        driver.get("https://premark-demo.bridge-teams.com/")
        # xpath of new button
        layout_wrapper = '//*[@id="layout-wrapper"]/div/div/div/div/div[2]/div[1]/div/div/a'
        # Waiting for home page is loading
        Newelement = wait.until(EC.presence_of_element_located((By.XPATH, layout_wrapper)))
        # verify the button
        self.assertTrue(Newelement)
        accordian = wait.until(EC.presence_of_element_located((By.XPATH, '//a[text()="Bridge Global"]')))
        collapse_class = accordian.get_attribute("class")
        if 'not-collapsed' not in collapse_class:
            self.waitThenScrollAndClick(driver,
                                        '//a[text()="Bridge Global"]')
            time.sleep(2)
        self.waitThenScrollAndClick(driver,
                                    '//*[contains(text(), "Bridge Global")]/ancestor::div[1]/div/div/p/div/div/table/tbody/tr[last()]/td[7]/ul/li/a')
        wait.until(EC.presence_of_element_located((By.ID, 'receipt_number__BV_label_')))
        property_value = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                    '//*[@id="property_management"]/div/div/div/div[2]/span[contains(text(), "Skyline Apartments")]')))
        self.assertTrue(property_value)
        self.waitThenScrollAndClick(driver, '//a[contains(text(), "Bewerk")]')
        wait.until(EC.presence_of_element_located((By.ID, 'location__BV_label_')))
        input_field = self.waitThenScrollAndClick(driver, '//*[@id="budget"]/div/div/input')
        sample_val = '66965.00'
        input_field.send_keys(sample_val)
        self.waitThenScrollAndClick(driver, '//button[contains(text(), "Bijwerken")]')

        wait.until(EC.presence_of_element_located((By.ID, 'receipt_number__BV_label_')))
        time.sleep(2)
        val = driver.find_element(By.XPATH, '//*[@id="budget"]/div/div/input').get_attribute('value')
        self.assertEqual(val, sample_val)
        time.sleep(2)
        driver.close()

    # automate scroll
    def waitThenScrollAndClick(self, driver, xpath):
        header_element = driver.find_element(By.TAG_NAME, 'header')
        additional_header_elem = driver.find_element(By.XPATH, '//*[@id="page-topbar"]/div[2]')
        elem = driver.find_element(By.XPATH, xpath)
        scroll_y_by = (elem.location_once_scrolled_into_view['y'] - (
                header_element.size['height'] + additional_header_elem.size['height']))
        driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
        current_element = None
        while True:
            try:
                current_element = WebDriverWait(driver, 455).until(EC.presence_of_element_located((By.XPATH, xpath)))
                current_element.click()
                break
            except ElementClickInterceptedException:
                continue
        return current_element


obj = ChromeDriverWindows()
obj.siteMethod()
