from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import shutil

# 복사된 프로필 경로 (임시 저장소로)
original_profile = r"C:\Users\박수똥\AppData\Local\Google\Chrome\User Data\Default"
selenium_profile = r"C:\Users\박수똥\AppData\Local\Google\Chrome\selenium_profile"

# 폴더 없으면 복사
if not os.path.exists(selenium_profile):
    shutil.copytree(original_profile, selenium_profile)

# 셀레니움 설정
chrome_options = Options()
chrome_options.add_argument(f"--user-data-dir={selenium_profile}")
chrome_options.add_argument("--profile-directory=Default")  # 복사한 프로필이 기본이라면 이대로

# 브라우저 실행
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://x.com")

input("✅ 로그인 상태 확인 후 엔터를 눌러주세요: ")
driver.quit()
