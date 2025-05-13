import time
import json
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def create_driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.page_load_strategy = "eager"

    driver = webdriver.Chrome(options=options)
    driver.execute_cdp_cmd(
        "Page.addScriptToEvaluateOnNewDocument",
        {
            "source": """
                Object.defineProperty(navigator, 'webdriver', {
                    get: () => undefined
                });
            """
        },
    )
    return driver

def load_cookies(driver, cookie_file):
    driver.get("https://x.com")
    with open(cookie_file, "r", encoding="utf-8") as f:
        cookies = json.load(f)
        for cookie in cookies:
            if "sameSite" in cookie and cookie["sameSite"] == "None":
                cookie["sameSite"] = "Strict"
            try:
                driver.add_cookie(cookie)
            except Exception as e:
                print(f"⚠️ 쿠키 추가 실패: {cookie.get('name')} - {e}")
    driver.get("https://x.com/home")
    time.sleep(5)

def scrape_tweets(driver, query, max_scrolls=30):
    encoded_query = query.replace(" ", "%20")
    url = f"https://x.com/search?q={encoded_query}&src=typed_query&f=live"
    driver.get(url)
    time.sleep(5)

    for _ in range(max_scrolls):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2.5)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    tweets = []
    for article in soup.find_all("article"):
        time_tag = article.find("time")
        if time_tag:
            created_at = time_tag["datetime"]
            text = article.get_text(separator=" ").strip()
            tweets.append([created_at, text])
    return tweets

def main():
    driver = create_driver()
    load_cookies(driver, "twitter_cookies.json")
    query = "포카 OR 응원봉 OR 굿즈"
    tweets = scrape_tweets(driver, query, max_scrolls=50)
    driver.quit()

    df = pd.DataFrame(tweets, columns=["created_at", "text"])
    df.to_csv("goods_tweets_with_cookies.csv", index=False, encoding="utf-8-sig")
    print(f"✅ 총 {len(df)}개의 트윗이 저장되었습니다.")

if __name__ == "__main__":
    main()
