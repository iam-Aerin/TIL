# Django ImageField 기반 인스타그램형 게시판 만들기

이 문서는 Django의 `ImageField`를 활용하여 이미지 업로드가 가능한 인스타그램 스타일의 게시판을 만드는 과정을 정리한 TIL입니다. 모델 설계부터 폼 처리, 이미지 저장까지 핵심 개념과 흐름을 정리했습니다.

---

## 🔹 핵심 개념 요약

- `ImageField`는 이미지를 저장하기 위한 Django 모델 필드
- 이미지 업로드를 위해 `Pillow` 패키지 설치 필요
- `MEDIA_URL`과 `MEDIA_ROOT` 설정을 통해 이미지 접근 및 저장 경로 설정
- 이미지 파일을 포함한 폼 데이터는 `request.FILES`로 전달됨
- 템플릿에서는 `{{ object.image.url }}`로 이미지 렌더링 가능
- 필요한 패키지 정리는 `requirements.txt`로 관리
- Bootstrap을 사용하면 간편하게 스타일링 가능

---

## 🔹 사전 준비

### 1. Pillow 설치
```bash
pip install Pillow
```

### 2. django-resized 설치 (프로필 이미지 리사이징 용도)
```bash
pip install django-resized
```
> 사용 예시는 아래 'accounts 앱 구성' 항목 참고

### 3. Bootstrap 5 사용
#### 방법 1: CDN 방식 (간단)
`base.html`의 `<head>`에 아래 코드 삽입:
```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
```

#### 방법 2: 패키지 설치 및 Django 연동
```bash
pip install django-bootstrap5
```
그리고 `settings.py`에 앱 추가:
```python
INSTALLED_APPS = [
    ...
    'django_bootstrap5',
]
```

템플릿에서 사용 시:
```django
{% load django_bootstrap5 %}
{% bootstrap_form form %}
```

---

## 🔹 settings.py 설정 (공통 설정)
```python
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

### URL 설정 (insta/urls.py)
```python
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
    path('accounts/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## 🔹 posts 앱 구성 (이미지 게시판)

### 모델 설계
```python
from django.db import models
from django.conf import settings
from django_resized import ResizedImageField

class Post(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = ResizedImageField(
        size=[500, 500],
        crop=['middle', 'center'],
        upload_to='image/%Y/%m'
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
```

> 게시글(Post)은 작성자(user)와 1:N 관계로 연결되어 있으며, 이미지 크기 조절을 위해 `ResizedImageField`를 사용하고 있습니다.

---

## 🔹 accounts 앱 구성 (사용자 정의 User 모델 + 프로필 이미지)

### models.py
```python
from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField

class User(AbstractUser):
    profile_image = ResizedImageField(
        size=[500, 500],
        crop=['middle', 'center'],
        upload_to='profile'
    )
```
> `django-resized` 라이브러리를 사용하여 프로필 이미지를 업로드 시 자동 리사이징 및 크롭 처리합니다.

### settings.py 설정 (accounts 전용 설정)
```python
# 사용자 정의 User 모델 적용
AUTH_USER_MODEL = 'accounts.User'
```
> `AbstractUser`를 상속한 커스텀 유저 모델을 사용하기 위한 필수 설정입니다. 앱 생성 후 마이그레이션 전에 반드시 지정해야 합니다.

---

## 🔹 템플릿 구성 예시

### create.html
```html
{% extends 'base.html' %}
{% load django_bootstrap5 %}

{% block body %}
  <form action="" method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {% bootstrap_form form %}
    <input type="submit" class="btn btn-primary" value="업로드">
  </form>
{% endblock %}
```

### index.html + 카드 분리
```html
{% for post in posts %}
  {% include '_card.html' %}
{% endfor %}
```

```html
<!-- _card.html -->
<div class="card">
  <img src="{{ post.image.url }}" alt="게시글 이미지" width="300">
  <p>{{ post.content }}</p>
</div>
```

---

## 🔹 템플릿에서 이미지 출력 예시
```html
<img src="{{ post.image.url }}" alt="게시글 이미지">
<img src="{{ user.profile_image.url }}" alt="프로필 이미지">
```
- 개발 모드에서만 `MEDIA_URL` 설정으로 이미지가 정상 출력됨

---

## 🔹 기타 필수 설정 및 관리

### .gitignore
```gitignore
media/
post_images/
profile/
```

### requirements.txt 저장
```bash
pip freeze > requirements.txt
```

---

## ✅ 요약

- 게시판(posts) 앱과 사용자 정보(accounts) 앱을 분리 구성
- `ImageField`, `ResizedImageField`를 적절히 활용해 이미지 업로드 및 크기 조절
- Bootstrap과 `django-bootstrap5`로 빠르게 스타일 적용
- `MEDIA_URL`, `MEDIA_ROOT` 설정은 공통적으로 사용됨
- 사용자 정의 유저 모델을 위해 `AUTH_USER_MODEL` 설정 필수
- 게시글(Post)은 `user` 필드를 통해 작성자와 연결됨
- `.gitignore`에 이미지 저장 폴더는 반드시 추가

---

