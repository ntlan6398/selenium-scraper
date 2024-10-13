from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd
def get_main_categories():
    website = "https://apps.shopify.com/"
    service = Service(executable_path="chromedriver")
    driver = webdriver.Chrome(service=service)
    driver.get(website)
    megaMenu = driver.find_element(By.ID, "AppStoreMegamenu")
    ul = megaMenu.find_element(By.TAG_NAME, "ul")
    aList = ul.find_elements(By.TAG_NAME, "a")
    spanList = ul.find_elements(By.TAG_NAME, "span")
    main_categories = []
    for i in range(aList.__len__()):
        category =spanList[i].get_attribute("innerHTML").strip()
        url = aList[i].get_attribute("href")
        main_categories.append({
        "category":category,
        "url":url})
    driver.quit()
    return main_categories
main_categories = get_main_categories()
# Create a DataFrame from the categories list
df = pd.DataFrame(main_categories)

# Create an ExcelWriter object
with pd.ExcelWriter("Shopify_Apps.xlsx", engine='openpyxl') as writer:
    # Write the DataFrame to the "Categories" sheet
    df.to_excel(writer, sheet_name="Categories", index=False)

print("Data saved to Shopify_Apps.xlsx in the 'Categories' sheet.")
