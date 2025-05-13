import time
import pickle
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# ✅ 브라우저 옵션 설정 (자동화 탐지 우회)
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=options)

# ✅ 탐지 우회용 JavaScript 삽입
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
    """
})

# ✅ 트위터 로그인 페이지 열기
driver.get("https://twitter.com/login")
print("🔐 로그인 후 인증까지 수동으로 완료하세요.")
time.sleep(120)

# ✅ 쿠키 저장
cookies = driver.get_cookies()
with open("twitter_cookies.pkl", "wb") as f:
    pickle.dump(cookies, f)

print("✅ 쿠키 저장 완료!")
driver.quit()
