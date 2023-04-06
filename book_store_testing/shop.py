#Shop: отображение страницы товара
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()
#шаг_2
my_account=driver.find_element_by_link_text("My Account")
my_account.click()
log_username=driver.find_element_by_id("username")
log_username.send_keys("gavrilapetrovic99@gmail.com")
log_password=driver.find_element_by_id("password")
log_password.send_keys("a340b777b")
login_button=driver.find_element_by_css_selector("[name='login']")
login_button.click()
#шаг_3
shop_tab=driver.find_element_by_link_text("Shop")
shop_tab.click()
#шаг_4
html_book=driver.find_element_by_css_selector(".post-181 h3")
html_book.click()
#шаг_5
book_head_name=driver.find_element_by_css_selector(".summary.entry-summary h1")
book_head_name_text=book_head_name.text
assert book_head_name_text == "HTML5 Forms"
driver.quit()
#
#
#Shop: количество товаров к категории
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()
#шаг_2
my_account=driver.find_element_by_link_text("My Account")
my_account.click()
log_username=driver.find_element_by_id("username")
log_username.send_keys("gavrilapetrovic99@gmail.com")
log_password=driver.find_element_by_id("password")
log_password.send_keys("a340b777b")
login_button=driver.find_element_by_css_selector("[name='login']")
login_button.click()
#шаг_3
shop_tab=driver.find_element_by_link_text("Shop")
shop_tab.click()
#шаг_4
html_cat=driver.find_element_by_css_selector(".cat-item.cat-item-19 a")
html_cat.click()
#шаг_5
items_count=driver.find_elements_by_css_selector(".products.masonry-done li")
if len(items_count) == 3:
    print("В категории 3 товара")
else:
    print("Ошибка! Количество товаров в корзине: "+str(len(items_count)))
driver.quit()



#Shop: сортировка товаров
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()
#шаг_2
my_account=driver.find_element_by_link_text("My Account")
my_account.click()
log_username=driver.find_element_by_id("username")
log_username.send_keys("gavrilapetrovic99@gmail.com")
log_password=driver.find_element_by_id("password")
log_password.send_keys("a340b777b")
login_button=driver.find_element_by_css_selector("[name='login']")
login_button.click()
#шаг_3
shop_tab=driver.find_element_by_link_text("Shop")
shop_tab.click()
#шаг_4
selector=driver.find_element_by_css_selector(".orderby").click()
default_sort=driver.find_element_by_css_selector("[value='menu_order']")
selected=default_sort.get_attribute ("selected")
print(selected)
#шаг_5
selector_a=driver.find_element_by_css_selector(".orderby").click()
option_a=driver.find_element_by_css_selector("[value='price-desc']").click()
#шаг_6
selector_b=driver.find_element_by_class_name("orderby")
#шаг_7
selector_b.click()
option=driver.find_element_by_css_selector("[value='price-desc']")
selected_a=option.get_attribute("selected")
print(selected_a)
driver.quit()


shop: отображение, скидка товара
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()
wait=WebDriverWait(driver, 10) #для сокращения записи ниже
#шаг_2
my_account=driver.find_element_by_link_text("My Account")
my_account.click()
log_username=driver.find_element_by_id("username")
log_username.send_keys("gavrilapetrovic99@gmail.com")
log_password=driver.find_element_by_id("password")
log_password.send_keys("a340b777b")
login_button=driver.find_element_by_css_selector("[name='login']")
login_button.click()
#шаг_3
shop_tab=driver.find_element_by_link_text("Shop")
shop_tab.click()
#шаг_4
book=driver.find_element_by_css_selector(".post-169 h3")
book.click()
#шаг_5_6
old_price=driver.find_element_by_css_selector(".price>del>span")
old_price_text=old_price.text
new_price=driver.find_element_by_css_selector(".price>ins>span")
new_price_text=new_price.text
assert old_price_text == "₹600.00"
assert new_price_text == "₹450.00"
#шаг_7
book_cover=wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")))
book_cover.click()
#шаг_8
cross_close=wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
cross_close.click()


#shop: проверка цены в корзине
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()
wait=WebDriverWait(driver, 10) #для сокращения записи ниже
#шаг_2
shop_tab=driver.find_element_by_id("menu-item-40")
shop_tab.click()
#шаг_3
add_to_bask=driver.find_element_by_css_selector(".post-165>a:nth-child(2)")
add_to_bask.click()
#шаг_4
item=driver.find_element_by_css_selector(".cartcontents")
item_text=item.text
price=driver.find_element_by_xpath("//span[@class='amount']")
price_text=price.text
assert item_text == "1 Item"
assert price_text == "₹350.00"
#шаг_5
cart=driver.find_element_by_id("wpmenucartli")
cart.click()
#шаг_6
subtotal=wait.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal"), "₹350.00"))
#шаг_7
total=wait.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total"), "₹357.00"))
driver.quit()


#shop: работва в корзине
import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(3)
#шаг_2
shop_tab=driver.find_element_by_id("menu-item-40")
shop_tab.click()
time.sleep(3)
#шаг_3 для добавления в корзину доступна только одна книга
driver.execute_script("window.scrollBy(0, 300);")
add_to_bask=driver.find_element_by_css_selector(".post-165>a:nth-child(2)")
add_to_bask.click()
#шаг_4
time.sleep(3)
cart=driver.find_element_by_id("wpmenucartli")
cart.click()
#шаг_5
time.sleep(2)
remove_btn=driver.find_element_by_css_selector("a.remove")
remove_btn.click()
time.sleep(2)
#шаг_6
undo=driver.find_element_by_link_text("Undo?")
undo.click()
time.sleep(2)
#шаг_7
quantity=driver.find_element_by_css_selector(".input-text.qty.text")
quantity.clear()
time.sleep(2)
quantity.send_keys("3")
#шаг_8
time.sleep(1)
update_bsk=driver.find_element_by_xpath("//input[@name='update_cart']")
update_bsk.click()
time.sleep(2)
#шаг_9
quan=driver.find_element_by_css_selector(".quantity input")
quan_value=quan.get_attribute("value")
assert quan_value == "3"
#шаг_10
time.sleep(2)
a_c=driver.find_element_by_xpath("//input[@name='apply_coupon']")
a_c.click()
time.sleep(2)
#шаг_11
message=driver.find_element_by_css_selector(".woocommerce-error li")
message_text=message.text
assert message_text == "Please enter a coupon code."
driver.quit()


#shop: покупка товара
import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(3)
#шаг_2
shop_tab=driver.find_element_by_id("menu-item-40")
shop_tab.click()
driver.execute_script("window.scrollBy(0, 300);")
time.sleep(2)
#шаг_3 для добавления доступна только одна книга
add_to_bask=driver.find_element_by_css_selector(".post-165>a:nth-child(2)")
add_to_bask.click()
time.sleep(2)
#шаг_4
cart=driver.find_element_by_id("wpmenucartli")
cart.click()
time.sleep(2)
#шаг_5
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
wait=WebDriverWait(driver, 10)
p_t_c=wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button.button")))
p_t_c.click()
#шаг_6
first_name=wait.until(
    EC.element_to_be_clickable((By.ID, "billing_first_name")))
first_name.send_keys("Vano")
last_name=driver.find_element_by_id("billing_last_name")
last_name.send_keys("Shvili")
email=driver.find_element_by_id("billing_email")
email.send_keys("Valeo@mail.com")
phone=driver.find_element_by_id("billing_phone")
phone.send_keys("111-222-444")
#country=driver.find_element_by_xpath("//div[@class='select2-drop-mask']")
#country.click()
#country_field=driver.find_element_by_id("s2id_autogen1_search")
#country_field.send_keys("India")
adress=driver.find_element_by_xpath("//input[@placeholder='Street address']")
adress.send_keys("broadway,10")
city=driver.find_element_by_id("billing_city")
city.send_keys("Mumbai")
zip=driver.find_element_by_id("billing_postcode")
zip.send_keys("1234")
#шаг_7
time.sleep(2)
driver.execute_script("window.scrollBy(0, 600);")
radiobtn=driver.find_element_by_id("payment_method_cheque")
radiobtn.click()
#шаг_8
place_order=driver.find_element_by_id("place_order")
place_order.click()
#шаг_9
head=wait.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
#шаг_10
tab=wait.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".method"), "Check Payments"))
driver.quit()
