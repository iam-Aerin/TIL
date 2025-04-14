# DAMF2 프로젝트: 다른 사람의 코드 클론 및 환경 설정 가이드

## 1. GitHub에서 코드 클론하기

```bash
git clone <레포지토리 URL>
```

## 2. VSCode로 프로젝트 열기

- 클론한 폴더를 VSCode에서 엽니다.
- 터미널을 열어 아래 과정을 진행합니다.

## 3. 가상환경 설정

```bash
python -m venv venv
```

### 가상환경 활성화 (Windows 기준)

```bash
source venv/Scripts/activate
```

> macOS/Linux는 `source venv/bin/activate`

## 4. 패키지 설치

```bash
pip install -r requirements.txt
```

## 5. .gitignore 설정

다음 항목들이 `.gitignore`에 포함되어 있어야 합니다:

```
venv/
__pycache__/
*.pyc
*.pyo
*.pyd
*.sqlite3
db.sqlite3
.DS_Store
migrations/
```

> `migrations/`는 공유하지 않아도 되지만, 만약 포함되어 있다면 아래 명령어로 마이그레이션을 적용하세요.

## 6. 마이그레이션 적용 (선택 사항)

```bash
python manage.py migrate
```

