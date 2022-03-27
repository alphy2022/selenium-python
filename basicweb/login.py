from selenium import webdriver
from unittest import TestCase

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class chromedriverwindows(TestCase):
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
        bvElement = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="complaints"]/div/textarea')))
        datrePicker = '//*[@id="notification_date"]/div/div'
        driver.find_element(By.XPATH, datrePicker).click()
        dateCollection = driver.find_elements(By.CLASS_NAME, 'mx-date-row')
        from datetime import datetime
        today = datetime.today().strftime('%Y-%m-%d')
        for eachField in dateCollection:
            for DateField in eachField.find_elements(By.TAG_NAME, 'td'):
                if (DateField.get_attribute("title") == today):
                    DateField.click()
                    break

        driver.find_element(By.ID, 'property_user').click()
        driver.find_element(By.XPATH, '//*[@id="property_user"]/div/div/div/div[2]/input').send_keys('br')
        wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="property_user"]/div/div/div/div[3]/ul/li[1]/span')))
        propert = driver.find_element(By.XPATH, '//*[@id="property_user"]/div/div/div/div[3]/ul/li[1]/span/span')
        if propert.text == 'Bridge Global':
            propert.click()

        driver.find_element(By.XPATH, '//*[@id="property_management"]/div/div/div/div[2]/input').click()
       # driver.find_element(By.zxPATH, '//*[@id="property_management"]/div/div/div/div[2]/input').send_keys('sk')
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="property_management"]/div/div/div[1]/div[3]/ul/li[1]/span/span')))
        driver.find_element(By.XPATH, '//*[@id="property_management"]/div/div/div[1]/div[3]/ul/li[1]/span/span').click()

        driver.find_element(By.XPATH, '//*[@id="reporter_name"]/div/input').send_keys('tester')

        driver.find_element(By.XPATH, '//*[@id="location"]/div/input').send_keys('kochi')

        driver.find_element(By.XPATH, '//*[@id="type_of_complaint"]/div/div/div/div[2]/input').click()
        driver.find_element(By.XPATH, '//*[@id="type_of_complaint"]/div/div/div/div[3]/ul/li[1]/span').click()

        driver.find_element(By.XPATH, '//*[@id="complaints"]/div/textarea').send_keys('test complaints....')

        element = driver.find_element(By.XPATH, '//*[@id="term"]/div/div/div/div[2]/input')
        action = ActionChains(driver)
        headerElement = driver.find_element(By.TAG_NAME, 'header')
        headerElementSixe  = headerElement.size
        driver.execute_script("arguments[0].focus();", element)
        action.move_to_element_with_offset(element, headerElementSixe['height'], 0).click().perform()
        driver.find_element(By.XPATH, '//*[@id="term"]/div/div/div[1]/div[3]/ul/li[1]').click()

        maintenanceElement = driver.find_element(By.XPATH, '//*[@id="maintenance"]/div/div/div[1]/div[2]/input')
        #driver.execute_script("arguments[0].scrollIntoView();", maintenanceElement)
        print(maintenanceElement.location_once_scrolled_into_view)
        print(headerElementSixe['height']/2)
        desired_y = (maintenanceElement.size['height'] / 2) + maintenanceElement.location['y']
        current_y = (driver.execute_script('return window.innerHeight') / 2) + driver.execute_script(
            'return window.pageYOffset')
        scroll_y_by = desired_y - current_y
        driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
        import time
        time.sleep(2)
       # driver.execute_script("window.scrollTo(0, arguments[0]);", maintenanceElement.location_once_scrolled_into_view['y'] - (headerElementSixe['height']/2))
        #driver.execute_script("arguments[0].focus();", maintenanceElement)
        actions = ActionChains(driver)
        #actions.move_to_element_with_offset(maintenanceElement, headerElementSixe['height'], 0).click().perform()
        driver.find_element(By.XPATH, '//*[@id="maintenance"]/div/div/div[1]/div[1]').click()
        #driver.execute_script("arguments[0].click()", maintenanceElement)
        driver.find_element(By.XPATH, '//*[@id="maintenance"]/div/div/div[1]/div[3]/ul/li[1]/span').click()



        wait.until(EC.visibility_of_element_located((By.XPATH, "adsgrthyjkuii")))


ff = chromedriverwindows()
ff.site_login()
