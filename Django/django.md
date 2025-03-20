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

##  1. RESTful이라는 문제?  
**RESTful하다**는 것은 **REST(Representational State Transfer)** 원칙을 따르는 API를 의미합니다. REST는 웹에서 데이터를 주고보는 방식으로, 다음과 같은 특징을 가지며 RESTful한 것으로 인정합니다.

### 💡 RESTful API의 태평 원칙  
1. **자원(Resource) 중심 설계**  
   - API는 **"무엇을 조작할 것인가?"**를 중심으로 설계  
   - ✅ `/users/`, `/articles/`, `/products/` 등 명사형 URL 사용  

2. **HTTP 메서드(Method) 사용**  
   | 동작 | HTTP 메서드 | RESTful URL 예시 |
   |------|------------|-----------------|
   | 데이터 조회 (Read) | `GET` | `/articles/` (전체 조회), `/articles/1/` (단각 조회) |
   | 데이터 생성 (Create) | `POST` | `/articles/` (새 글 생성) |
   | 데이터 수정 (Update) | `PUT` / `PATCH` | `/articles/1/` (1번 글 수정) |
   | 데이터 삭제 (Delete) | `DELETE` | `/articles/1/` (1번 글 삭제) |

3. **URL은 동생(X), 명사(O)**  
   - ❌ `/getUsers`, `/updateUser/1` (비 RESTful)  
   - ✅ `/users/`, `/users/1/` (RESTful)  

4. **Stateless (상황 저장 X)**  
   - 서버가 클라이언트의 상황을 기억하지 않음  
   - 모든 요청은 **도대체적**이며 필요한 데이터를 포함해야 함  

5. **일괄된 응답 형식 (JSON 사용)**  
   ```json
   {
       "id": 1,
       "title": "Django RESTful API",
       "content": "RESTful API는 자원 중심으로 설계됩니다."
   }
   ```

