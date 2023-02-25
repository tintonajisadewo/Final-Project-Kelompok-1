
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTestpimemployee():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testpimemployee(self):
    self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    self.driver.set_window_size(958, 1039)
    self.driver.find_element(By.LINK_TEXT, "PIM").click()
    self.driver.find_element(By.LINK_TEXT, "Add Employee").click()
    self.driver.find_element(By.NAME, "firstName").click()
    self.driver.find_element(By.NAME, "firstName").send_keys("Budi")
    self.driver.find_element(By.NAME, "middleName").send_keys("Mulya")
    self.driver.find_element(By.NAME, "lastName").send_keys("Prasetya")
    self.driver.find_element(By.CSS_SELECTOR, ".bi-plus").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-switch-input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-input--focus").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-input--focus").send_keys("Budii")
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-input--focus").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-input--focus").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-input--focus").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".oxd-input--focus")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-input--focus").send_keys("budi12")
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-input--focus").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-input--focus").send_keys("Budi#123")
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-input--focus").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-input--focus").send_keys("Budi#123")
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-button--secondary").click()
  
