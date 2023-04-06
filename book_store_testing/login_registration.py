#registration_login: регистрация аккаунта
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()
#шаг_2
my_account=driver.find_element_by_link_text("My Account")
my_account.click()
#шаг_3
reg_email_field=driver.find_element_by_id("reg_email")
reg_email_field.send_keys("gavrilapetrovic99@gmail.com")
#шаг_4
reg_password_field=driver.find_element_by_id("reg_password")
reg_password_field.send_keys("a340b777b")
#шаг_5
register_btn=driver.find_element_by_xpath("//input[@name='register']")
register_btn.click()
driver.quit()

#registration_login: логин в систему
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()
#шаг_2
my_account=driver.find_element_by_link_text("My Account")
my_account.click()
#шаг_3
log_username=driver.find_element_by_id("username")
log_username.send_keys("gavrilapetrovic99@gmail.com")
#шаг_4
log_password=driver.find_element_by_id("password")
log_password.send_keys("a340b777b")
#шаг_5
login_button=driver.find_element_by_css_selector("[name='login']")
login_button.click()
#шаг_6
logout_btn=driver.find_element_by_link_text("Logout")
logout_btn_text=logout_btn.text
assert logout_btn_text == "Logout"
driver.quit()