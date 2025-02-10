from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv
import time
from datetime import datetime

# Set up Selenium
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode (no UI)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Amazon product URL (replace with the actual URL)
url = "https://www.amazon.in/MADE-INDIA-Years-Business-Enterprise/dp/9357020683/"
driver.get(url)

# Extract product price
try:
    price = driver.find_element(By.CSS_SELECTOR, "span.a-price-whole").text
    print("Price:", price)
except:
    print("Price not found!")

driver.quit()



now = datetime.now()
date_str = now.strftime("%Y-%m-%d")
time_str = now.strftime("%H:%M:%S")

with open("product_price.csv", "a", newline="") as file:
   writer = csv.writer(file)
   writer.writerow([date_str, time_str, price])

print(f"Saved to CSV: {date_str}, {time_str}, {price}")