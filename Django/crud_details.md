# Django에서 CRUD 구현하기

## 0. Setting

### 🖥 **터미널에서 입력해야 하는 코드**

#### 1️⃣ 가상 환경 설정
```bash
python -m venv venv  # 가상 환경 생성
source venv/Scripts/activate  # Windows
source venv/bin/activate      # macOS/Linux
```

#### 2️⃣ Django 설치
```bash
pip install django
```

#### 3️⃣ 프로젝트 및 앱 생성
```bash
django-admin startproject crud .  # 프로젝트 생성
django-admin startapp posts  # 앱 생성
```

#### 4️⃣ 마이그레이션 적용 (DB 반영)
```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 1. Django 프로젝트 설정

### 📝 **파일을 찾아서 직접 입력해야 하는 코드**

#### 1️⃣ `settings.py` 수정 (앱 등록)
📂 **파일 위치:** `crud/settings.py`
```python
INSTALLED_APPS = [
    ...
    'posts',  # posts 앱 추가
]
```

#### 2️⃣ `urls.py` 수정 (앱 연결)
📂 **파일 위치:** `crud/urls.py`
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),  # posts 앱의 URL 관리
]
```

#### 3️⃣ `posts/urls.py` 생성 및 설정
📂 **파일 위치:** `posts/urls.py` (파일이 없으면 새로 생성)
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # 메인 페이지
    path('post/new/', views.create_post, name='create_post'),  # 새 게시글 작성
    path('post/<int:post_id>/edit/', views.update_post, name='update_post'),  # 게시글 수정
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),  # 게시글 삭제
]
```

#### 4️⃣ `models.py` 설정 (모델링)
📂 **파일 위치:** `posts/models.py`
```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)  # 제목
    content = models.TextField()  # 내용
    created_at = models.DateTimeField(auto_now_add=True)  # 생성일
    updated_at = models.DateTimeField(auto_now=True)  # 수정일

    def __str__(self):
        return self.title
```

---

## 2. Django에서 CRUD 구현하기

### 🖥 **터미널에서 입력해야 하는 코드**

#### 마이그레이션 적용 (DB에 모델 반영)
```bash
python manage.py makemigrations
python manage.py migrate
```

#### Django Shell에서 데이터 추가 (테스트용)
```bash
python manage.py shell
```
```python
from posts.models import Post
post = Post.objects.create(title="첫 번째 게시글", content="Django ORM으로 CRUD 구현하기")
```

---

## 3. CRUD 기능 구현 (Django ORM 활용)

### 📝 **파일을 찾아서 직접 입력해야 하는 코드**

#### 1️⃣ **데이터 생성 (Create) - View 설정**
📂 **파일 위치:** `posts/views.py`
```python
from django.shortcuts import render, redirect
from .models import Post

def create_post(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        Post.objects.create(title=title, content=content)
        return redirect("post_list")
    return render(request, "posts/create_post.html")
```

#### 2️⃣ **데이터 조회 (Read) - View 설정**
📂 **파일 위치:** `posts/views.py`
```python
def post_list(request):
    posts = Post.objects.all()
    return render(request, "posts/post_list.html", {"posts": posts})
```

#### 3️⃣ **데이터 수정 (Update) - View 설정**
📂 **파일 위치:** `posts/views.py`
```python
from django.shortcuts import get_object_or_404

def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        post.save()
        return redirect("post_list")
    return render(request, "posts/update_post.html", {"post": post})
```

#### 4️⃣ **데이터 삭제 (Delete) - View 설정**
📂 **파일 위치:** `posts/views.py`
```python
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        post.delete()
        return redirect("post_list")
    return render(request, "posts/delete_post.html", {"post": post})
```

---

## 4. CRUD와 Django ORM의 관계 정리
| CRUD 연산 | Django ORM 코드 |
|-----------|----------------|
| **Create** | `Post.objects.create(title="제목", content="내용")` |
| **Read** | `Post.objects.all()` / `Post.objects.get(id=1)` |
| **Update** | `post.title = "변경된 제목"; post.save()` |
| **Delete** | `post.delete()` |

---

## **최종 정리**
- **터미널에서 입력해야 하는 코드** ✅ : Django 설치, 프로젝트 생성, 앱 생성, 마이그레이션, Django Shell 사용 등
- **파일을 찾아서 직접 입력해야 하는 코드** 📝 : `settings.py`, `urls.py`, `models.py`, `views.py` 등의 코드 작성


