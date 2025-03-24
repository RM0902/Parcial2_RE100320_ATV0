from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Test1LOGIN():
    def setup(self):
        self.driver = webdriver.Firefox()
        self.driver.set_window_size(1318, 701)

    def teardown(self):
        self.driver.quit()

    def run_login_test(self):
        for i in range(100):
            print(f"Intento #{i + 1}")
            self.driver.get("http://localhost/PHP-MYSQL-User-Login-System/login.php")

            # Ingresar email
            self.driver.find_element(By.NAME, "email").click()
            self.driver.execute_script("document.getElementsByName('email')[0].value = 'rodrigomanuel99@gmail.com';")

            # Ingresar password
            self.driver.find_element(By.NAME, "password").click()
            self.driver.execute_script("document.getElementsByName('password')[0].value = '1234';")

            # Hacer click en el botón de login
            self.driver.find_element(By.ID, "submit").click()
            time.sleep(1)

            # Logout (si aplica)
            try:
                self.driver.find_element(By.ID, "dropdownMenuLink").click()
                self.driver.find_element(By.LINK_TEXT, "Logout").click()
                time.sleep(1)
            except:
                print("No se encontró el menú de logout, puede que el login haya fallado.")
                continue

if __name__ == "__main__":
    test = Test1LOGIN()
    test.setup()
    try:
        test.run_login_test()
    finally:
        test.teardown()
