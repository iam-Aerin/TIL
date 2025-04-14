## 웹 크롤링

```ubuntu
damf2/automation/1.upbit-api/ 파일에서 작업중중
```

- API, 정적 사이트, 동적사이트

## API
- 업비트 API: 시세 현재가 조회

![alt text](image-2.png)

https://docs.upbit.com/kr

```
https://api.upbit.com/v1/ticker?markets=KRW-BTC
```

![alt text](image-4.png)

---
## Static web: 정적 사이트에서 크롤링
- `lotto.py`

https://dhlottery.co.kr/common.do?method=main

![동행복권 메인페이지에서 당첨 번호 가져오기](image-5.png)
> 개발자 도구를 통해 내가 필요한 정보 (html코드)를 확인하기

![alt text](image-6.png)

---
## Dynamic web: 동적 사이트에서 크롤링