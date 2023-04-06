from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get("https://practice.automationtesting.in/")
driver.maximize_window()
driver.implicitly_wait(5)
#шаг_2
driver.execute_script("window.scrollBy(0, 600);")
#шаг_3
selenium_ruby_book=driver.find_element_by_css_selector("div.woocommerce>ul>li>a>img")
selenium_ruby_book.click()
#шаг_4
reviews_tab=driver.find_element_by_css_selector("li.reviews_tab")
reviews_tab.click()
#шаг_5
five_stars=driver.find_element_by_class_name("star-5")
five_stars.click()
#шаг_6
review_field=driver.find_element_by_id("comment")
review_field.send_keys("Nice book!")
#шаг_7
name_field=driver.find_element_by_id("author")
name_field.send_keys("Igor")
#шаг_8
email_field=driver.find_element_by_id("email")
email_field.send_keys("valeo@mail.com")
#шаг_9
submit_btn=driver.find_element_by_id("submit")
submit_btn.click()
driver.quit()