from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

# MODIFY THIS PATH TO MATCH THE LOCATION OF YOUR SAVED CHROMEDRIVER AND OPERATING SYSTEM
CHROMEDRIVER_PATH = "/Users/bls/Development/chromedriver"
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
service = ChromeService(executable_path=CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)


# FIND ELEMENTS IN THE BROWSER
driver.get("https://www.python.org/")

search_bar = driver.find_element(By.NAME, "q")
print(search_bar.get_attribute("placeholder"))

logo = driver.find_element(By.CLASS_NAME, "python-logo")
print(logo.size)

documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
print(documentation_link.text)

diversity_footer_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[2]/a')
print(diversity_footer_link.text)

# CHALLENGE: FIND UPCOMING EVENTS AND CREATE A DICTIONARY FOR DATES AND NAME OF LATEST EVENTS
upcoming_event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
for time in upcoming_event_times:
    print(time.text)

upcoming_event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
for name in upcoming_event_names:
    print(name.text)

# CREATE DICTIONARY OF UPCOMING EVENTS
events = {}
for n in range(len(upcoming_event_times)):
    events[n] = {
        "time": upcoming_event_times[n].text,
        "name": upcoming_event_names[n].text,
    }
print(events)

driver.quit()
