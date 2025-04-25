from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

options = Options()

# 화면 사이즈 크게 키우기
options.add_argument("--start-maximized")
# 화면 꺼지지 않게 하기
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)

url = "https://naver.com"

driver.get(url)
# 웹사이트를 열고 시간 두고 검색
time.sleep(3)

# 1
# 검색창 input id=query
# query = driver.find_element(By.ID, 'query')

# # 입력할 검색어
# query.send_keys('오늘 날씨')
# time.sleep(2)

# # 검색 버튼 클릭
# search_btn = driver.find_element(By.CSS_SELECTOR, '#search-btn')
# search_btn.click()
# time.sleep(2)

# 2
driver.find_element(By.ID, 'query').send_keys('오늘 날씨')
time.sleep(2)

# driver.find_element(By.CSS_SELECTOR, '#search-btn').click()
driver.find_element(By.ID, 'query').send_keys(Keys.ENTER)
time.sleep(2)

# 스크린 샷 찍기
driver.save_screenshot('screenshots/today_weather.png')

# 창 닫기
driver.quit()


