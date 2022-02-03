from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

CARBON_MCC_URL = 'https://www.mcc-berlin.net/fileadmin/data/clock/carbon_clock.htm'

def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options=chrome_options)
  return driver


def get_time_countdown(driver):
  TIMECOUNTDOWN_DIV_ID = 'timecountdown'
  driver.get(CARBON_MCC_URL)

  # Clicked 1.5 Deg Celcius Scenario Button
  button = driver.find_elements_by_xpath('/html/body/div/div/div[2]/ul[1]/li[2]/a')[0]
  button.click()
  
  timecountdown = driver.find_elements(By.ID, TIMECOUNTDOWN_DIV_ID)
  return timecountdown

def parse_page(driver):

  time_countdown_years = driver.find_element(By.ID, 'years').text 
  time_countdown_months = driver.find_element(By.ID, 'months').text
  time_countdown_days = driver.find_element(By.ID, 'days').text
  time_countdown_hours = driver.find_element(By.ID, 'hours').text
  time_countdown_minutes = driver.find_element(By.ID, 'minutes').text
  time_countdown_seconds = driver.find_element(By.ID, 'seconds').text
  time_countdown_milliseconds = driver.find_element(By.ID, 'milliseconds').text

  return {
    'years': time_countdown_years,
    'months': time_countdown_months,
    'days': time_countdown_days,
    'hours': time_countdown_hours,
    'minutes': time_countdown_minutes,
    'seconds': time_countdown_seconds,
    'milliseconds': time_countdown_milliseconds
  }

if __name__ == "__main__":
  print('Creating driver')
  driver = get_driver()

  print('Fetching Carbon MCC Page')
  time_countdown = get_time_countdown(driver)
  
  print(f'Found {len(time_countdown)} Time Count Down')

  print('Parsing the MCC Page')
  page_data = parse_page(driver)
  
  print('years:', page_data['years'])
  print('months:', page_data['months'])
  print('days:', page_data['days'])
  print('hours:', page_data['hours'])
  print('minutes:', page_data['minutes'])
  print('seconds:', page_data['seconds'])
  print('milliseconds:', page_data['milliseconds'])

  print('Finished.')
