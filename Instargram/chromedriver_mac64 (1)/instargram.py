import time
import os
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument(
    "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36")
driver = webdriver.Chrome(os.path.join(
    os.path.dirname(os.getcwd()), 'chromedriver'))
driver.get("https://www.instagram.com")

time.sleep(10)
print('로그인')

id_box = driver.find_element(By.CSS_SELECTOR,
                             "#loginForm > div > div:nth-child(1) > div > label > input")
password_box = driver.find_element(By.CSS_SELECTOR,
                                   "#loginForm > div > div:nth-child(2) > div > label > input")
login_button = driver.find_element(By.CSS_SELECTOR,
                                   "#loginForm > div > div:nth-child(3) > button")

# 우측 상
print("로그인 진행중")
act = ActionChains(driver)
act.send_keys_to_element(id_box, 'windy7271@naver.com').send_keys_to_element(
    password_box, 'Sb813792!!@').click(login_button).perform()
print("로그인 성공")
time.sleep(20)

print("나중에 정보 저장 시도") ## 로그인 정보 저장 팝업 처리
try:
    not_now_button = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='나중에 하기']")))
    not_now_button.click()
except:
    print("오류발생")

print("알림설정 끄기 시도")
try:
    turn_off_button = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='나중에 하기']")))
    turn_off_button.click()
except:
    print("알림 끄기 오류발생")


print("프로필로 이동 시도")
try:
    # 프로필 페이지로 이동합니다.
    profile = 'windy_tour'
    profile_link = driver.find_element(By.XPATH, f'//a[@href="/{profile}/"]')
    profile_link.click()
    print("프로필 페이지로 이동 성공")
except NoSuchElementException:
    print("프로필 페이지가 존재하지 않습니다.")
except ElementClickInterceptedException:
    print("프로필 페이지로 이동하는 과정에서 클릭 오류가 발생했습니다.")

print("프로필로 이동 성공, 팔로워,팔로잉 데이터 크롤링")


followers = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//a[@href='/windy_tour/followers/']//span")))
followings = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//a[@href='/windy_tour/following/']//span")))
print("Followers: " + followers.text)
print("Followings: " + followings.text)


# 팔로워 버튼 클릭하기
followers = driver.find_element(By.XPATH, "//a[@href='/windy_tour/followers/']")
followers.click()
time.sleep(5)
print("팔로워 가져오기")
# 팔로워 목록이 모두 로딩될 때까지 스크롤을 내리며 팔로워 가져오기
while True:
    try:
        print("1")
        # 팝업 윈도우 가져오기
        popup = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='isgrP']")))

        # 팔로워 목록 가져오기
        print("2")
        followers_list = popup.find_elements(By.XPATH, "//li[@class='wo9IH']//a[@title]")

        print("3")
        # 스크롤을 끝까지 내림
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", popup)
        print("4")
        # 일정 시간 대기
        time.sleep(5)

    except NoSuchElementException:
        print(NoSuchElementException)
        break



