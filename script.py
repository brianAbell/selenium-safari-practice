#NOTE: typically we would have 'Inspect Elements' open to know ref names

from selenium import webdriver
# import due to needing to simulate keyboard interactions
from selenium.webdriver.common.keys import keys

# set up the driver for Safari
driver = webdriver.Safari()

# navigate to Google's homepage
driver.get("https://www.google.com")

# find the search box element by its 'name' attribute
search_box = driver.ind_element_by_name("q")

# input "OpenAI ChatGPT" into the search box
search_box.send_keys("OpenAI ChatGPT")

# simulate pressing the "Return" key on your keyboard
search_box.send_keys(Keys.RETURN)

# wait for 5 seconds to see results
driver.implicitly.wait(5)

# close browser
driver.quit()
