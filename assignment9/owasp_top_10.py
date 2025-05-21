from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url = "https://owasp.org/www-project-top-ten/"
driver.get(url)

time.sleep(5)

results = []

try:
    vulnerabilities = driver.find_elements(By.XPATH, "//h2[contains(text(), 'Top 10 Web Application Security Risks')]/following-sibling::ul[1]/li")
    
    for vuln in vulnerabilities:
        if 'A' in vuln.text and any(digit in vuln.text for digit in "0123456789"):
            title = vuln.text
            link = vuln.get_attribute('href')
            
            vuln_info = {
                "Title": title,
                "Link": link
            }
            
            results.append(vuln_info)
    
except Exception as e:
    print(f"Error extracting vulnerabilities: {e}")

print("\nOWASP Top 10 Vulnerabilities:")
for i, vuln in enumerate(results, 1):
    print(f"{i}. {vuln['Title']} - {vuln['Link']}")

df = pd.DataFrame(results)

df.to_csv("owasp_top_10.csv", index=False)
print("\nData written to owasp_top_10.csv")

driver.quit()