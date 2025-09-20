
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestNutapos():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_nutapos(self):
    self.driver.get("https://nutacloud.com/authentication/loginv2")
    self.driver.set_window_size(964, 475)
    self.driver.find_element(By.NAME, "idperusahaan").click()
    self.driver.find_element(By.NAME, "idperusahaan").send_keys("Adjiecorp")
    self.driver.find_element(By.NAME, "username").click()
    self.driver.find_element(By.NAME, "username").send_keys("testingAdjie")
    self.driver.find_element(By.ID, "input-password").click()
    self.driver.find_element(By.ID, "input-password").send_keys("Testing12345")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.execute_script("window.scrollTo(0,367.3333435058594)")
    self.driver.find_element(By.LINK_TEXT, "Adjiecorp").click()
    self.driver.find_element(By.CSS_SELECTOR, ".user-info > .nav-profile-outlet-name").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".fa-caret-square-o-up")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
  
