### 셀레니움
> 웹브라우저를 코드로 조작하기 위한 프로그램 :https://www.selenium.dev/
파이썬 버전으로 다운 https://pypi.org/project/selenium/

`damf2/autonmation/3.dynamic-web/0.melon` 
> 동적 웹 페이지에서 데이터 수집하기

## 멜론차트에서 데이터 가져오기

https://www.melon.com/

https://www.melon.com/chart/index.htm

1. chrome (browser)
2. chrome driver (browser driver)
3. selenium (driver)
4. python (browser driver)

```
linux 환경에서 돌아가는 chrome driver를 다운 받아야함.
```

:  python 코드로 chrome을 조작하기

chrome
```bash
# download
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
```

```bash
# install
sudo apt --fix-broken install -y
sudo dpkg -i google-chrome-stable_current_amd64.deb
```

chrome driver
```bash
wget https://storage.googleapis.com/chrome-for-testing-public/135.0.7049.84/linux64/chromedriver-linux64.zip
```

---

## css 에서 요소 지정해서 가져오기 연습: 
https://css-speedrun.netlify.app/

> 첫번째 li 태그 가져오기
![css speedrun](/assets/image-8.png)

> 특정 클래스 제외하기
![특정 클래스 제외](/assets/image-9.png)

> 3, 5, 7번째 li 태그 가져오기
![3, 5, 7번째 li 태그 가져오기 (수식표현)](/assets/image-10.png)

> 모든 자식 요소 가져오기
![alt text](/assets/image-11.png)

> 같은 attribute 값의 요소 가져오기
![alt text](/assets/image-12.png)

> 형제 선택자


> #one, #two, #five, #six, #nine
![alt text](/assets/image-14.png)

![alt text](/assets/image-13.png)

> 인접 형제 선택자
![alt text](/assets/image-15.png)

> div#foo > div.foo
![alt text](/assets/image-16.png)

> div선택, 형제 선택, 제외 조건 추가가
![alt text](/assets/image-17.png)

---
_#내맘대로TIL챌린지 #동아일보 #미디어프론티어 #글로벌소프트웨어캠퍼스 #GSC신촌_

_글로벌소프트웨어캠퍼스와 동아일보가 함께 진행하는 챌린지입니다._
