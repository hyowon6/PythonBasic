from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 드라이버 설정
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# 웹페이지 해당 주소 이동
driver.get('https://www.naver.com')


# 네이버 로그인
def naver_login():
    try:
        # 로그인 버튼 클릭
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.MyView-module__link_login___HpHMW'))
        )
        login_button.click()

        # 아이디와 비밀번호 입력
        user_id = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'id'))
        )
        user_pw = driver.find_element(By.ID, 'pw')

        # 아이디를 한 글자씩 입력
        for char in 'y020606':  # 네이버 ID
            user_id.send_keys(char)
            time.sleep(0.1)  # 각 문자 입력 후 잠시 대기

        time.sleep(1)  # 잠시 대기

        # 비밀번호를 한 글자씩 입력
        for char in 'yh14!':  # 네이버 PW
            user_pw.send_keys(char)
            time.sleep(0.1)  # 각 문자 입력 후 잠시 대기

        # 로그인 버튼 클릭
        login_submit = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'log.login'))
        )
        login_submit.click()

        time.sleep(5)  # 로그인 완료 대기
    except Exception as e:
        print(f"로그인 중 오류 발생: {e}")


# 네이버 메일 확인
def check_mail():
    try:
        # 메일 페이지로 이동
        mail_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.nav[title="메일"]'))
        )
        mail_link.click()

        time.sleep(5)  # 메일 페이지 로드 대기

        # 최근 메일 확인 (메일 목록 첫 번째 항목 기준)
        recent_mail = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.mailList .mail_item:nth-child(1)'))
        )
        print("최근 메일 제목:", recent_mail.text)

    except Exception as e:
        print(f"메일 확인 중 오류 발생: {e}")


# 실행
naver_login()
check_mail()
