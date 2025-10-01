from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Launch the browser
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # Open the website
    driver.get('https://weathershopper.pythonanywhere.com')

    # Verify the page title contains the expected text
    assert 'Current Temperature' in driver.title, "Page title does not match expected!"

    # Wait until the button is present (up to 10 seconds)
    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'btn-primary'))
    )

    # Print the visible text of the button
    print("Button contains text:", button.text)

except TimeoutException:
    print("The button was not found within the given time!")
except AssertionError as e:
    print("Error:", e)
finally:
    # Close the browser
    driver.quit()
