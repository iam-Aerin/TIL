
*5월 1주차*

- logstash
> `logstash.md`

_#내맘대로TIL챌린지 #동아일보 #미디어프론티어 #글로벌소프트웨어캠퍼스 #GSC신촌_

_글로벌소프트웨어캠퍼스와 동아일보가 함께 진행하는 챌린지입니다._


---
# `logstash.md`
# ELK stack

## logstash
- 설치 (8.18 version)
: `wget https://artifacts.elastic.co/downloads/logstash/logstash-8.18.0-linux-x86_64.tar.gz`

- unzip
: `tar -zxvf logstash-8.18.0-linux-x86_64.tar.gz` 

> logstash, elasticsearch, kibana 를 각 터미널에서 실행
```shell
bin/elasticsearch
```
```shell
bin/kibana
```

`localhost:5601 에서 동작 확인`

## git clone `insta` (django) 로 log 관리하기위해서 

- damf2 git repository에서 clone 해오기

`cd damf2` 위치에서
```shell
git clone https://github.com/DAMF2/insta.git
```

- 가상 환경 활성화후  `requirements.txt` 에 있는 패키지들 설치
```
ubuntu@smart:~/damf2/insta$ python -m venv venv
ubuntu@smart:~/damf2/insta$ source venv/bin/activate
```

- `pip install -r requirements.txt`
```shell
(venv) ubuntu@smart:~/damf2/insta$ pip install -r requirements.txt
```

```python 
pythonmanage.py migrate
```

```python
python manage.py runserver
``` 

- `localhost:8000` 접속 후 동작 확인
> insta 페이지 로그인, 게시물 생성 등의 log가 terminal에 찍히는것을 확인할 수 있다.

- log 설정
> `insta 폴더 안의 'settings.py` 파일에서 `LOGGING` 항목을 수정


LOGGING = {
    'version': 1, 
    'disable_existing_loggers': False,
    
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'django.log'},
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    
    'loggers': {
        'django.server': {
            'handlers': ['file', 'console'],
            'level': 'INFO',
            'propagate': False,
        }
    }
}

---
# `visualisation_kibana.md`
# Kibana로 시각화하기
> Kibana sample data(e-commerce)데이터로 시각화 연습


- `metric`으로 `Sum of taxful_total_price`를 시각화

![kibana_visualisation_sum](/assets/sum_kibana.png)

![alt text](/assets/bar_categories_order_date.png)

![alt text](/assets/kibana_product_quantity.png)

- 일주일 전 products.quantity 의 sum을 시각화화
![alt text](image-4.png)

- 수식 (이번주 매출액 - 지난주 매출액)
![alt text](/assets/kibana_formula(sum).png)

- 음수는 빨강/ 양수는 파랑으로 색 설정정
![alt text](/assets/kibana_colour_range.png)