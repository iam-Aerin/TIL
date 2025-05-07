
*5월 1주차*

- logstash
> `logstash.md`

_#내맘대로TIL챌린지 #동아일보 #미디어프론티어 #글로벌소프트웨어캠퍼스 #GSC신촌_

_글로벌소프트웨어캠퍼스와 동아일보가 함께 진행하는 챌린지입니다._


---
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

cd damf2 위치에서
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

- localhost:8000 접속 후 동작 확인
> insta 페이지 로그인, 게시물 생성 등의 log가 terminal에 찍히는것을 확인할 수 있다.