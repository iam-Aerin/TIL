# Django Authentication 
## Django Authentication 기능 및 게시판 구현

## 개요

오늘은 Django의 **auth 모듈**을 활용하여 **계정 생성, 로그인, 로그아웃** 기능을 구현하고, **게시물 작성 기능이 포함된 게시판 페이지**를 제작했습니다.

이를 통해 사용자 인증 흐름과 Django의 내장 기능들을 활용한 개발 과정을 경험했습니다.

---

## 1. 기본 프로젝트 및 앱 설정

### 1.1 프로젝트 및 앱 생성

```bash
django-admin startproject auth
cd auth
python manage.py startapp accounts
python manage.py startapp articles
```

### 1.2 앱 등록

`settings.py`의 `INSTALLED_APPS`에 `accounts`, `articles` 앱을 추가합니다.

---

## 2. 사용자 인증 기능 구현

### 2.1 URL 설정 (`accounts/urls.py`)

```python
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
```

### 2.2 View 작성 (`accounts/views.py`)

```python
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            next_url = request.GET.get('next')
            return redirect(next_url or 'articles:index')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('accounts:login')
```

### 2.3 템플릿 작성

**signup.html**:

```html
{% extends 'base.html' %}
{% block body %}
<form action="" method="POST">
    {% csrf_token %}
    {{ form }}
    <input type="submit" value="Sign Up">
</form>
{% endblock %}
```

**login.html**:

```html
{% extends 'base.html' %}
{% block body %}
<form action="" method="POST">
    {% csrf_token %}
    {{ form }}
    <input type="submit" value="Log In">
</form>
{% endblock %}
```

---

## 3. 게시물 작성 기능 구현

### 3.1 URL 설정 (`articles/urls.py`)

```python
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
]
```

### 3.2 View 작성 (`articles/views.py`)

```python
from django.shortcuts import render, redirect
from .forms import ArticleForm

def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    return render(request, 'create.html', {'form': form})
```

### 3.3 Form 작성 (`articles/forms.py`)

```python
from django.forms import ModelForm
from .models import Article

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
```

### 3.4 템플릿 작성 (`create.html`)

```html
{% extends 'base.html' %}
{% block body %}
<form action="" method="POST">
    {% csrf_token %}
    {{ form }}
    <input type="submit" value="Create Article">
</form>
{% endblock %}
```

---

## 4. 전체 URL 연결 (`auth/urls.py`)

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('articles/', include('articles.urls')),
]
```

---

## 5. 결과 확인

- **회원가입**: `/accounts/signup/`
- **로그인**: `/accounts/login/`
- **로그아웃**: `/accounts/logout/`
- **게시글 작성**: `/articles/create/`

---

## 6. 오늘의 학습 요약

- Django의 `auth` 모듈을 활용해 사용자 인증 기능(회원가입, 로그인, 로그아웃)을 구현했습니다.
- `ModelForm`을 사용하여 게시물 작성 폼을 간편하게 생성했습니다.
- URL 네임스페이스(`app_name`)와 템플릿 태그(`{% url %}`)를 활용해 깔끔한 라우팅을 구성했습니다.

---

## 💡 추가로 알아두면 좋은 개념들

| 개념 | 설명 |
|------|------|
| `login_required` 데코레이터 | 로그인하지 않은 사용자가 특정 페이지에 접근하지 못하게 제한할 수 있습니다. 게시물 작성 페이지에 적용 가능 |
| `User` 모델 커스터마이징 | 기본 `User` 모델을 커스터마이징해서 프로필 정보(예: 닉네임, 프로필 이미지 등)를 추가할 수 있습니다 |
| `request.user` | 로그인된 사용자의 정보를 가져올 수 있는 속성입니다. 게시글 작성 시 작성자를 자동으로 지정할 때 유용 |
| 메시지 프레임워크 (`django.contrib.messages`) | 로그인/로그아웃/회원가입 등의 결과 메시지를 사용자에게 보여줄 수 있습니다 |

