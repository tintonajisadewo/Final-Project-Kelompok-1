import unittest
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#Tes Login 
class LoginTest(unittest.TestCase):

    def setUp(self):
        # Inisialisasi driver
        self.driver = webdriver.Chrome(ChromeDriverManager().install())



    def test_login(self):
        # Membuka halaman login
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        self.assertIn("OrangeHRM", self.driver.title)

        # Mengisi form login
        time.sleep(3)
        username_input = self.driver.find_element(By.NAME, "username")
        username_input.clear()
        username_input.send_keys("Admin")

        password_input = self.driver.find_element(By.NAME,"password")
        password_input.clear()
        password_input.send_keys("admin123")
        time.sleep(1)

        # Klik tombol login
        login_button = self.driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")
        login_button.click()

        time.sleep(3)

        # Verifikasi login berhasil
        welcome_text = self.driver.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[1]/div[1]/span/h6")
        self.assertIn("Dashboard", welcome_text.text)

        time.sleep(2)

 # Masuk menu PIM > Employee List
        self.driver.get ("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")

        time.sleep(4)

# Mengisi Employee Name
        name_input = self.driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input")
        name_input.clear()
        name_input.send_keys("Wahid H")

        time.sleep(3)

#Klik tombol Search
        search_button = self.driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]")
        search_button.click()

        time.sleep(3)

#Klik tombol Reset
        reset_button = self.driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[1]")
        reset_button.click()

        time.sleep(4)

    def tearDown(self):
        # Tutup browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()