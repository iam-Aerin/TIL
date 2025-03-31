# 📸 Django ImageField 기반 인스타그램형 게시판 만들기

이 문서는 Django의 `ImageField`를 활용하여 이미지 업로드가 가능한 인스타그램 스타일의 게시판을 만드는 과정을 정리한 TIL입니다. 모델 설계부터 폼 처리, 이미지 저장까지 핵심 개념과 흐름을 정리했습니다.

---

## 🔹 핵심 개념 요약

- `ImageField`는 이미지를 저장하기 위한 Django 모델 필드
- 이미지 업로드를 위해 `Pillow` 패키지 설치 필요
- `MEDIA_URL`과 `MEDIA_ROOT` 설정을 통해 이미지 접근 및 저장 경로 설정
- 이미지 파일을 포함한 폼 데이터는 `request.FILES`로 전달됨
- 템플릿에서는 `{{ object.image.url }}`로 이미지 렌더링 가능
- 필요한 패키지 정리는 `requirements.txt`로 관리

---

## 🔹 사전 준비

### 1. Pillow 설치

```bash
pip install Pillow
```

### 2. settings.py 설정

```python
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_URL = '/image/'
MEDIA_ROOT = BASE_DIR / 'image'  # 이미지 파일은 프로젝트 루트의 image/ 폴더에 저장됨
```

### 3. URL 설정

#### (1) 프로젝트 루트의 `insta/urls.py`

```python
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

> 개발 환경에서만 동작하며, `/image/` 경로로 업로드된 미디어 파일 제공

---

## 🔹 모델 설계

```python
from django.db import models

class Post(models.Model):
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/')  # image/post_images/ 경로에 저장
    created_at = models.DateTimeField(auto_now_add=True)
```

---

## 🔹 Form 연결

```python
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'image']
```

---

## 🔹 View 흐름

```python
from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post

# 게시글 목록
def index(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'posts/index.html', {'posts': posts})

# 게시글 작성
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
    else:
        form = PostForm()
    return render(request, 'posts/create.html', {'form': form})
```

---

## 🔹 템플릿 구성

### `posts/templates/index.html`

```html
{% extends 'base.html' %}

{% block body %}
  {% for post in posts %}
    {% include '_card.html' %}  <!-- 카드 UI 분리 -->
  {% endfor %}
{% endblock %}
```

### `posts/templates/_card.html`

```html
<div class="card">
  <img src="{{ post.image.url }}" alt="게시글 이미지" width="300">
  <p>{{ post.content }}</p>
</div>
```

### `posts/templates/create.html`

```html
{% extends 'base.html' %}

{% block body %}
    <form action="" method="POST" enctype="multipart/form-data">
        {% csrf_token %}
        {{ form }}
        <input type="submit">
    </form>
{% endblock %}
```

> 이미지 파일을 업로드하는 폼에서는 반드시 `enctype="multipart/form-data"` 속성이 포함되어야 합니다.
> 또한 `{{ form }}`으로 ModelForm과 연동된 필드가 자동 생성됩니다.

---

## 🔹 템플릿에서 이미지 렌더링

```html
<img src="{{ post.image.url }}" alt="게시글 이미지">
```

- 개발 모드에서만 `MEDIA_URL` 설정으로 이미지가 정상 출력됨

---

## 🔹 파일 업로드 주의사항 정리

- `<form>`에는 `enctype="multipart/form-data"` 필수
- `request.FILES`로 이미지 데이터를 받을 수 있도록 view 설정 필요

---

## 🔹 Git 관리 주의사항 (`.gitignore`)

- 이미지 파일은 보통 Git에 포함시키지 않음
- 아래 항목을 `.gitignore`에 추가

```gitignore
image/
post_images/
```

---

## 🔹 패키지 관리

- 프로젝트에 설치된 라이브러리를 다른 개발자가 동일하게 설치할 수 있도록

```bash
pip freeze >> requirements.txt
```

---

## ✅ 요약

- `ImageField`는 이미지 업로드 필드이며, 업로드 파일은 `request.FILES`로 처리
- `Pillow` 패키지 설치가 필수
- `MEDIA_URL`, `MEDIA_ROOT`는 반드시 설정 필요하며, 개발환경에서만 서빙됨
- 컴포넌트 단위 템플릿(`_card.html`)으로 구성하면 유지보수가 쉬움
- `.gitignore`로 이미지 파일 폴더는 Git에서 제외
- `create.html`에서 파일 업로드를 위한 폼 구성 시 `enctype` 필수
- `pip freeze >> requirements.txt`로 환경 동기화

---

