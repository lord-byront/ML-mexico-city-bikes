from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import re
import time

# Setup headless browser with Selenium
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)

# Load Ecobici site
url = "https://ecobici.cdmx.gob.mx/mapa/"
driver.get(url)
time.sleep(5)

# Expand the station list
accordion = driver.find_element(By.CSS_SELECTOR, ".collapsible-header")
accordion.click()
time.sleep(1)

# Get full HTML after expansion
html = driver.page_source
driver.quit()

# Parse with BeautifulSoup
soup = BeautifulSoup(html, "html.parser")
station_links = soup.select("a.btn-to-station")

# Extract and process
data = []
for link in station_links:
    text = link.text.strip()

    # New regex: allow multiple numbers like 107-108
    match = re.match(r'(CE)[\s-]?(\d{3}(?:[-–]\d{3})?)\s+(.+?)\s*[–-]\s*(.+)', text)
    if match:
        prefix, number, street1, street2 = match.groups()
        data.append({
            "Prefix": prefix,
            "Number": number.strip(),
            "Street 1": street1.strip(),
            "Street 2": street2.strip()
        })
    else:
        data.append({
            "Prefix": "",
            "Number": "",
            "Street 1": text,
            "Street 2": ""
        })

# Save as CSV with UTF-8 BOM for Excel compatibility
df = pd.DataFrame(data)
df.to_csv("ecobici_stations.csv", index=False, encoding="utf-8-sig")
print("✅ CSV created with multi-number handling: ecobici_stations.csv")


