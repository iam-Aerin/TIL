# Django의 URL과 HTML 렌더링 관계

## 1. Django의 MTV 패턴
Django는 **MTV (Model-Template-View) 패턴**을 기반으로 웹 애플리케이션을 개발합니다.
- **Model (모델)**: 데이터베이스와의 상호작용을 담당
- **Template (템플릿)**: HTML 파일을 사용하여 데이터를 표시
- **View (뷰)**: 비즈니스 로직을 처리하고 데이터를 템플릿에 전달

MTV 패턴에서 URL은 **View**를 연결하며, View는 **Template**을 렌더링하는 역할을 합니다.

## 2. Django URL과 View의 흐름
Django의 URL과 View는 다음과 같은 과정으로 동작합니다:
1. 사용자가 특정 URL을 요청
2. Django의 `urls.py`에서 해당 URL 패턴과 연결된 View를 찾음
3. View는 데이터를 처리하고, HTML 템플릿을 렌더링하여 응답 반환

## 3. Django URL과 View 연동하기

### 3.1 URL 설정하기 (`urls.py`)
Django에서 URL은 `urls.py`에서 관리됩니다.
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # 홈페이지 URL
    path('about/', views.about, name='about'),  # about 페이지 URL
]
```

### 3.2 View 생성 (`views.py`)
View는 사용자의 요청을 처리하고 HTML 템플릿을 렌더링하는 역할을 합니다.
```python
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # home.html 템플릿을 렌더링

def about(request):
    return render(request, 'about.html')  # about.html 템플릿을 렌더링
```

### 3.3 HTML 템플릿 (`templates/home.html`)
Django는 템플릿 엔진을 통해 데이터를 동적으로 HTML에 삽입할 수 있습니다.
```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>Home</title>
</head>
<body>
    <h1>홈페이지</h1>
    <p>안녕하세요! Django 기반 웹사이트입니다.</p>
    <a href="{% url 'about' %}">About 페이지로 이동</a>
</body>
</html>
```

### 3.4 템플릿에서 URL 활용
Django 템플릿에서는 `{% url '이름' %}`을 사용하여 `urls.py`에서 정의한 URL을 참조할 수 있습니다.
```html
<a href="{% url 'home' %}">홈으로</a>
<a href="{% url 'about' %}">소개 페이지</a>
```

## 4. Django의 URL, View, HTML 관계 요약

| 역할 | 파일 | 설명 |
|------|------|------|
| URL 관리 | `urls.py` | URL과 View를 매핑 |
| 데이터 처리 | `views.py` | 요청을 처리하고 HTML을 렌더링 |
| HTML 출력 | `templates/` | 사용자가 보는 웹페이지 |

--- 
### Django REST Framework과 RESTful API 개념 정리  

---
### 📌 Django REST Framework과 RESTful API 개념 정리  

---

## 📝 1. RESTful이란?  
**RESTful하다**는 것은 **REST(Representational State Transfer)** 원칙을 따르는 API를 의미합니다. REST는 웹에서 데이터를 주고받는 방식으로, 다음과 같은 특징을 가집니다.

### 💡 RESTful API의 핵심 원칙  
1. **자원(Resource) 중심 설계**  
   - API는 **"무엇을 조작할 것인가?"**를 중심으로 설계  
   - ✅ `/users/`, `/articles/`, `/products/` 등 명사형 URL 사용  

2. **HTTP 메서드(Method) 사용**  
   | 동작 | HTTP 메서드 | RESTful URL 예시 |
   |------|------------|-----------------|
   | 데이터 조회 (Read) | `GET` | `/articles/` (전체 조회), `/articles/1/` (단건 조회) |
   | 데이터 생성 (Create) | `POST` | `/articles/` (새 글 생성) |
   | 데이터 수정 (Update) | `PUT` / `PATCH` | `/articles/1/` (1번 글 수정) |
   | 데이터 삭제 (Delete) | `DELETE` | `/articles/1/` (1번 글 삭제) |

3. **URL은 동사(X), 명사(O)**  
   - ❌ `/getUsers`, `/updateUser/1` (비 RESTful)  
   - ✅ `/users/`, `/users/1/` (RESTful)  

4. **Stateless (상태 저장 X)**  
   - 서버가 클라이언트의 상태를 기억하지 않음  
   - 모든 요청은 **독립적**이며 필요한 데이터를 포함해야 함  

5. **일관된 응답 형식 (JSON 사용)**  
   ```json
   {
       "id": 1,
       "title": "Django RESTful API",
       "content": "RESTful API는 자원 중심으로 설계됩니다."
   }
   ```

---

## 📝 2. Django에서 CSRF 토큰이란?
### 💡 CSRF (Cross-Site Request Forgery) 보호
CSRF(Cross-Site Request Forgery)는 웹 애플리케이션의 보안을 위협하는 공격 기법 중 하나로, 사용자의 의도와 무관하게 공격자가 요청을 전송할 수 있도록 하는 취약점입니다. Django는 CSRF 공격을 방지하기 위해 **CSRF 토큰**을 사용합니다.

### 🔹 CSRF 토큰이 필요한 이유
- Django는 **POST, PUT, DELETE 요청**에 대해 CSRF 토큰이 없으면 요청을 차단합니다.
- 모든 HTML 폼에서 `{% csrf_token %}`을 포함해야 합니다.
- CSRF 검증이 실패하면 `403 Forbidden` 오류가 발생합니다.

### 🔹 Django에서 CSRF 토큰 사용 방법
#### ✅ 1) HTML 폼에 `{% csrf_token %}` 추가
```html
<form action="/articles/create/" method="POST">
    {% csrf_token %}  <!-- CSRF 보호를 위한 필수 태그 -->
    <input type="text" name="title">
    <button type="submit">제출</button>
</form>
```

#### ✅ 2) Django 뷰에서 `request` 객체를 포함하여 렌더링
```python
from django.shortcuts import render

def create(request):
    return render(request, 'articles/create.html')  # request 객체를 전달해야 CSRF 토큰이 생성됨
```

#### ✅ 3) CSRF 토큰을 AJAX 요청에 포함하기 (비동기 요청)
```javascript
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

fetch('/articles/create/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken  // CSRF 토큰을 헤더에 포함
    },
    body: JSON.stringify({ title: 'My New Article' })
});
```

#### ✅ 4) 테스트용으로 CSRF 검증 비활성화 (⚠️ 추천하지 않음)
```python
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # CSRF 검증 비활성화
def create(request):
    return render(request, 'articles/create.html')
```
> **⚠️ 주의:** `@csrf_exempt`는 보안상 위험하므로 실제 운영 환경에서는 사용하지 않는 것이 좋습니다.

### 🔹 `settings.py`에서 CSRF 관련 설정 변경
```python
CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8000',  # 로컬 개발 환경
    'https://yourdomain.com',  # 배포 환경
]
```

---

## 결론
- Django REST Framework는 RESTful한 API를 쉽게 만들 수 있도록 도와주는 도구입니다.
- RESTful API는 **자원 중심**, **HTTP 메서드 활용**, **Stateless** 원칙을 따라야 합니다.
- Django에서는 보안을 위해 **CSRF 토큰**을 사용해야 하며, 모든 **POST 요청 폼**에 `{% csrf_token %}`을 추가해야 합니다.
- AJAX 요청 시 `X-CSRFToken` 헤더를 포함하여 전송해야 합니다.

이제 Django에서 RESTful API를 더 안전하고 효율적으로 설계할 수 있습니다! 🚀


