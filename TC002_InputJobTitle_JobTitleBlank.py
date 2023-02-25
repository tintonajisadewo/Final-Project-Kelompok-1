import unittest
import time
import pyautogui
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select

class TestLogin(unittest.TestCase): 
    

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_success_login(self): 
        # steps        
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") #buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin")
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-slot > div.orangehrm-login-form > form > div:nth-child(3) > div > div:nth-child(2) > input").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # klik tombol sign in
        time.sleep(1)

        #MenuDashboard
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").click() #klik Menu Admin     
        time.sleep(1)  
        browser.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span/i').click() 
        time.sleep(1)
        browser.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[1]/a').click()  
        time.sleep(1)
        browser.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div[1]/div/button').click() #klik add
        time.sleep(5)

        #InputFileUpload
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/input").send_keys("")
        time.sleep(5)
        browser.find_element(By.CSS_SELECTOR,'#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div:nth-child(2) > div > div:nth-child(2) > textarea').send_keys("Menghandle Semua QA, Baik Automation maupun Manual")
        time.sleep(5)
        #uploadBerkas
        browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[2]/div[1]/i[1]").click()
        time.sleep(4) #waiting for window popup to open
        pyautogui.write(r"123.jpg") #path of File
        pyautogui.press('enter')
        time.sleep(5)
        browser.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[4]/div/div[2]/textarea').send_keys("Iya Ini Final Project Ku")   
        time.sleep(5)
        browser.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[5]/button[2]').click() #klik Save
        time.sleep(20)
 
    
def tearDown(self): 
        time.sleep(5)
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()

