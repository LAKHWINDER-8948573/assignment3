from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Create a WebDriver instance for Google Chrome
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://www.canadacomputers.com/")
time.sleep(2)

# Find the search bar and send the search query
search_bar = driver.find_element_by_id("cc_quick_search")
search_bar.send_keys("AMD Ryzen 3")
search_bar.send_keys(Keys.RETURN)

# Wait for the search results to load
driver.implicitly_wait(10)

# Find and click the link for "shop products on the navigation"
shop_products_link = driver.find_element_by_link_text("Shop Products")
shop_products_link.click()

# Find and click the link for all deals
all_deals_link = driver.find_element_by_class_name("pagelink-brand pl-1")
all_deals_link.click()

# Find and click the link to view the cart
view_cart_button = driver.find_element_by_class_name("cart-icon")
view_cart_button.click()

# Find and click the link for store pickup or delivery
store_pickup_deliver_link = driver.find_element_by_class_name("ml-1 font-0_8")
store_pickup_deliver_link.click()

# Close the browser when done
driver.quit()
