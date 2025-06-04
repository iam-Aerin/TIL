# 프로젝트
## 5월 5주차 목표

이번 주: 마이페이지 구현부터 이미지 업로드까지, 사용자 경험 중심의 기능들을 중심으로 작업 계획
/ 백엔드 로직, 프론트엔드 스타일링, 외부 데이터 연동까지 균형 잡힌 개발이 목표

---

### 🔹 마이페이지 기능 개발
- 찜한 아티스트 불러오기
- 팔로잉 / 팔로워 기능 연결
- 내가 작성한 덕담 / 덕팜 / 덕생 게시글 연결

### 🔹 1:1 채팅 기능 구축
- 기본 채팅 구조 및 URL 라우팅 구상
- 메시지 실시간 송수신 처리 고려

### 🔹 생일 관련 기능
- 트위터 API / 덕플레이스 / 오프메이 기반 생일 카페 데이터 크롤링
- 생일 캘린더 & 배너 출력 기능

---

## 🔹 데이터 및 모델링 작업
- 각 Post 모델을 Artist / Member와 연결 (ForeignKey 또는 ManyToManyField 고려)

---

## 🔹 페이지 및 UI 개선
- 덕담 / 덕팜의 detail.html을 통일감 있게 수정
- 각 카테고리별 create.html의 CSS 스타일 통일

---

## 🔹 검색 및 필터링
- 상품별 필터링 기능 (※ 검색 기능 우선 개발 후 필터링은 추후 논의)

---

## 🔹 소셜 로그인(OAuth)
- 네이버 / 카카오 로그인 기능 추가  
  참고 URL: [Django OAuth 검색 결과](https://www.google.com/search?q=django+oauth)

---

## 🔹 이미지 업로드 및 편집
### 이미지 여러 장 업로드
- 하나의 포스트에 여러 이미지 등록 가능하도록 모델 수정
  - S3를 통한 이미지 저장
  - 게시물과 이미지 간 1:N 구조 모델링

### 이미지 편집 기능
- Cropper.js 활용한 클라이언트 사이드 이미지 편집 시도
- 또는 원본 이미지 저장 → 수정 → 표시 흐름 고려

---

## 🔹 기타 기능
- 마이페이지와 프로필 페이지 구분
  - URL 예시: `/accounts/my` 접속 시 본인 마이페이지 열람 가능하도록 구현
- User 모델 또는 Post 기본값 등 default 설정 수정

---

##  포인트
- 모델 간 연결(관계 정의)과 사용자 경험(UI 흐름)을 동시에 고려해야 하는 작업이 많음.
- 이미지 처리 기능은 사용자 중심 UX를 위해 우선순위 높게 두고 시도할 것.
- 일정상 중요한 기능부터 순차적으로 마무리하고, 디테일은 이후 보완.

---

# 6월 1주차 TIL

---

## 진행 파일 목록

`project_diary.md`

_#내맘대로TIL챌린지 #동아일보 #미디어프론티어 #글로벌소프트웨어캠퍼스 #GSC신촌_

_글로벌소프트웨어캠퍼스와 동아일보가 함께 진행하는 챌린지입니다._

---
## 프로젝트 진행
- `project_diary.md` 참고

- 이번주 프로젝트 TO DO
---
# 📌 TIL 챌린지 - 6월 1주차: 포카 거래 UI/UX 현실화 문제와 기술적 해결 구상

## 문제 배경

현재 운영 중인 '어덕해' 서비스의 핵심 기능 중 하나인 **포토카드(포카) 중고거래**는, 기존 중고거래 플랫폼의 구조를 일부 차용하고 있다. 즉, 물건 1개에 게시글 1개, 이미지 1장 또는 다중 이미지에 수동 설명 입력 방식

하지만 실제 트위터(X) 기반 포카 거래자들은 **절대로 포카를 1장씩 따로 찍어 등록하지 않을 것으로 예상.**

- 보통 4~8장의 포토카드를 한 장의 사진에 묶어서 올리고,
- 텍스트에는 `리노 2000, 현진 1500, 한 3000` 등의 가격만 적음
- 이미지 기반이고, 개별 포카에 대한 정렬이나 검색 기능은 없음

이러한 현실적인 사용 패턴과 비교했을 때, 지금의 덕팜 UI/UX는 실사용 흐름과 괴리가 있음  
'편한 포카 거래의 장'이라는 기획 의도에 맞게 **사용자 중심의 구조적 리디자인**이 필요함을 인식

---

## 문제 요약

- 포토카드를 여러 장 찍은 이미지 1장을 등록 → 텍스트에 가격만 적는 구조가 트위터 거래의 표준
- 현행 덕팜 구조(이미지 1장 + 설명 1개)는 사용자의 실제 습관에 맞지 않음
- 실사용자들이 오히려 X를 더 편하게 느끼는 결과를 초래할 수 있음

---

## 해결 방향: 포카 묶음 이미지 → 자동 분할 + 가격 태깅

### 1. 이미지 내 포카 자동 검출 및 분할

**목표**: 묶음 사진 속 포카 개별 영역을 인식하고 잘라내서 보여주는 기능 도입

**기술 접근**:
- YOLOv8, Detectron2 같은 객체 탐지 모델을 이용해 포카 영역 검출
- 검출된 각 영역을 crop한 썸네일로 저장
- 사용자는 각 썸네일마다 가격만 입력하면 자동으로 등록 가능

```python
from ultralytics import YOLO

model = YOLO('yolov8n.pt')  # pretrained or custom-trained on 포카 dataset
results = model('multi_card.jpg')
results.crop(save=True)  # crop된 포카들 자동 저장
```

---
-> 업로드 UI 흐름 설계: 
1. 판매자가 포카 묶음 이미지 업로드
2. 백엔드에서 자동 검출 및 분할
3. 프론트엔드에서 썸네일 미리보기 + 가격 입력창 자동 생성
4. 확인 후 저장 → 포카 개별 게시물로 등록

| 기능 요소    | 기술 제안                                                   |
| -------- | ------------------------------------------------------- |
| 포카 검출    | YOLOv8, Detectron2, OpenCV                              |
| 이미지 업로드  | Django ImageField + JS 비동기 처리                           |
| 가격 입력 UI | JavaScript로 동적 input 생성                                 |
| 데이터 저장   | Post 모델 확장: `crop_coords`, `price`, `origin_image` 필드 등 |
| 미리보기 UI  | CropperJS 또는 Canvas 기반 프리뷰 지원                           |

-MVP 단계별 설계
| 단계  | 기능              | 난이도  | 설명                   |
| --- | --------------- | ---- | -------------------- |
| 1단계 | 멀티 이미지 업로드      | ★☆☆  | 기존 구조 개선, 다중 업로드 가능  |
| 2단계 | 수동 Crop UI      | ★★☆  | 판매자가 직접 crop → 가격 입력 |
| 3단계 | AI 포카 인식 자동화    | ★★★  | YOLOv8 기반 커스텀 학습 필요  |
| 4단계 | OCR 기반 가격 자동 추출 | ★★★★ | 이미지 내 숫자 인식 → 자동 입력  |
---

## 이번 주 주요 과제

- 기능별로 전반적인 마무리 작업을 진행하면서, 포카 거래 UX 고도화에 대한 방향성 고민을 시작.
- 특히 **X(구 Twitter) 기반 거래 관행**과 차별화된 방식으로, 다수의 포카를 묶음 이미지로 등록하고 자동화된 UX 제공을 위한 기술/서비스 구조 검토가 중심.

---

## ✅ 완료 항목

- static/image 디렉터리 `.gitignore` 해제
- 생일 캘린더 / 생일 배너 적용
- FAQ 모달 드래그 가능하게 수정
- 각 포스트 모델에 artist / member 연결 완료



## 새롭게 제기된 고민: “포카 묶음 이미지의 거래 방식 개선”

### ❗ 문제 인식
- X(트위터) 기반 포카 거래는 "여러 장을 한 장의 사진에 담아 올리는 방식"이 일반적.
- 기존 덕팜 구조는 일반 중고거래처럼 **“이미지 1장 + 설명 1개”** 방식이라, 실사용자 거래 패턴과 맞지 않음.
- 즉, **유저가 포카 하나씩 따로 찍어서 등록하지 않는다**는 점이 문제 발생의 핵심.

### 해결 방향 제안

#### 1. 이미지 자동 분할 (포카 인식)
- 업로드된 1장의 이미지에서 포카 2장 이상이 있는 경우:
  - OpenCV 또는 Python 기반 이미지 분할 로직 적용 (기본적인 contour detection)
  - PIL, numpy, `cvlib`, `ultralytics/yolov5` + custom fine-tuning 등도 고려 가능

#### 2. 개별 포카 단위 가격 설정 UI
- 분할된 이미지 각각에 사용자가 **가격을 직접 입력**할 수 있도록 프론트엔드에서 Grid UI 제공
- 예: `crop된 썸네일 + input` 구성으로 loop 처리

#### 3. 백엔드 저장 구조
- 이미지 테이블(FarmImage)을 그대로 활용하되, `parent_image`, `is_auto_cropped`, `crop_coords`, `price` 필드 추가
- 향후 AI 기반 인식 정확도가 올라가면 OCR 기반 아티스트 자동 태깅도 가능

#### 4. 구매자 UX 개선
- 이미지에 마우스를 올리면 가격/멤버 등 정보가 뜨는 인터랙션
- 구매자는 묶음 이미지 안에서 **필요한 포카만 클릭 → 장바구니 추가** 가능하게

#### 5. 기존 방식과 비교되는 장점
- 개별 게시물 없이 묶음 이미지 하나로 효율적 등록
- 포카만 정확히 인식해 **불필요한 배경/손/책상 제거 가능**
- 추후 AI 모델 추가 시: 아티스트/멤버 인식 → 자동 태깅까지 확장 가능

---
# Django에서 '좋아요' (찜하기) 기능 구현

오늘은 Django 웹 애플리케이션에서 '찜하기' (좋아요) 기능을 구현하고 문제를 해결한 과정을 정리

## 1. 데이터 모델 수정
'찜하기' 기능을 구현하기 위해, `BdayCafe` 모델과 연관된 `CafeFavorite` 모델을 생성. 이 모델은 사용자가 찜한 카페를 저장하고 관리하는 역할

```python
class CafeFavorite(models.Model):
    """카페 즐겨찾기"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cafe = models.ForeignKey(BdayCafe, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'cafe')  # 같은 카페에 대해 한 번만 찜할 수 있도록 설정
```

## 2. 찜하기 토글 API 뷰
찜하기 버튼을 클릭할 때마다, 사용자가 해당 카페를 찜 목록에 추가하거나 제거하는 API가 동작합니다. 이를 위해 toggle_favorite_ajax라는 뷰를 추가했습니다.

API 동작:
찜 추가: 사용자가 카페를 찜하면 CafeFavorite 모델에 새로운 항목을 추가합니다.

찜 제거: 이미 찜한 상태에서 다시 찜하기 버튼을 클릭하면 해당 항목을 삭제합니다.

```
@login_required
@require_POST
@csrf_protect
def toggle_favorite_ajax(request, cafe_id):
    """찜하기 토글 API"""
    try:
        cafe = get_object_or_404(BdayCafe, id=cafe_id, status='approved')
        
        # 찜하기 토글
        favorite, created = FavoriteCafe.objects.get_or_create(user=request.user, cafe=cafe)
        
        if not created:  # 이미 찜한 상태면 제거
            favorite.delete()
            is_favorited = False
            message = "찜 목록에서 제거했어요!"
        else:  # 찜 추가
            is_favorited = True
            message = "찜 목록에 추가했어요!"
        
        # 찜 목록 업데이트
        my_favorite_cafes = BdayCafe.objects.filter(
            favoritecafes__user=request.user,
            status='approved'
        ).order_by('-favoritecafes__created_at')
        
        favorites_html = render_to_string(
            'ddoksang/components/_favorites_section.html',
            {'my_favorite_cafes': my_favorite_cafes, 'user': request.user},
            request=request
        )
        
        response_data = {
            'success': True,
            'is_favorited': is_favorited,
            'message': message,
            'favorites_html': favorites_html,
        }
        
        return JsonResponse(response_data)
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)

```

## 3. Frontend 연동 (JavaScript)
찜하기 버튼을 클릭하면 AJAX를 통해 서버와 통신을 하여 찜하기 상태를 갱신하고, 페이지 내에서 실시간으로 반영됩니다.

`favorite.js`

```javascript
class FavoriteManager {
    constructor() {
        this.isSubmitting = false;
        this.favoriteStates = new Map();
        this.callbacks = [];
        this.init();
    }

    init() {
        // 이벤트 리스너 등록
        document.addEventListener('click', (e) => {
            const favoriteBtn = e.target.closest('[data-favorite-btn]');
            if (!favoriteBtn || this.isSubmitting) return;

            const cafeId = favoriteBtn.dataset.cafeId;
            if (cafeId) {
                this.toggleFavorite(cafeId);
            }
        });
    }

    async toggleFavorite(cafeId) {
        if (this.isSubmitting) return;
        this.isSubmitting = true;

        const csrfToken = this.getCSRFToken();
        const response = await fetch(`/ddoksang/cafe/${cafeId}/toggle-favorite/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken,
            },
        });

        const data = await response.json();
        if (data.success) {
            this.updateAllButtons(cafeId, data.is_favorited);
            this.executeCallbacks(cafeId, data.is_favorited);
            this.showToast(data.message, 'success');
        } else {
            this.showToast(data.error, 'error');
        }

        this.isSubmitting = false;
    }

    updateAllButtons(cafeId, isFavorited) {
        // 버튼 상태 업데이트 (하트 아이콘, 색상 변경)
        const buttons = document.querySelectorAll(`[data-favorite-btn][data-cafe-id="${cafeId}"]`);
        buttons.forEach(button => {
            button.innerHTML = isFavorited ? '♥' : '♡';
            button.style.color = isFavorited ? '#ef4444' : '#6b7280';
        });
    }

    showToast(message, type) {
        // 사용자에게 토스트 메시지 표시
        alert(message); // 간단한 메시지로 대체
    }

    getCSRFToken() {
        return document.querySelector('[name=csrfmiddlewaretoken]').value;
    }
}

// 초기화
window.favoriteManager = new FavoriteManager();
```

> 중요 포인트:
AJAX 요청: JavaScript에서 찜하기 버튼 클릭 시, AJAX 요청을 통해 서버로 데이터를 전송하고 응답을 받아 UI를 실시간으로 갱신합니다.

서버 응답: 서버는 찜 상태 변경 결과를 JSON 형식으로 반환하고, 이를 바탕으로 UI를 업데이트합니다.

## 4. 관련 URL 설정
Django의 urls.py 파일에서 toggle_favorite 뷰를 처리하는 URL을 설정

```python
# 찜하기 토글 URL
path('cafe/<int:cafe_id>/toggle-favorite/', views.toggle_favorite_ajax, name='toggle_favorite'),

```
=> Django의 ForeignKey와 related_name을 활용해 사용자가 찜한 카페를 관리하고, JavaScript와 AJAX를 통해 사용자에게 실시간으로 업데이트된 찜 상태를 반영할 수 있음.
---
## 다음 주 추진 목표에 반영할 TODO (체크리스트 업데이트)

### 기능 구조 및 UX
- [ ] 공통 helpers 구조 설계
- [ ] 댓글 수정 기능 구조 기획
- [ ] 리뷰 작성 페이지 분리 구조 검토 (작성 vs 내 리뷰)
- [ ] 매너 리뷰는 거래 후만 가능하도록 흐름 제한
- [ ] 공식 팬 인증 사진 자동처리 구조 검토

### 이미지/포카 처리
- [ ] 포카 묶음 이미지에서 개별 포카 자동 인식 및 분할 기능 기획
- [ ] 각 포카 단위 가격 입력 가능한 UI 설계
- [ ] 이미지 모델에 crop 정보, 가격 등 메타데이터 저장 구조 설계
- [ ] 구매자가 포카별로 선택하여 거래 가능한 인터랙션 기획

### 덕팜 기능
- [ ] 1:1 채팅 기능
- [ ] 결제 API 연동
- [ ] 분철 멤버별 가격 설정 모델 설계
- [ ] 상세 검색 기능 (덕팜/덕담)
- [ ] 상품별 필터링 기능 (검색 우선)

---

## 기타 마이너 개선 및 회원 관련

- [ ] 다중 이미지 업로드 완성 및 S3 연동
- [ ] cropper.js 등 이미지 편집 도구 검토
- [ ] 회원가입 시 이메일 유효성/닉네임 중복 확인 기능
- [ ] 네이버 간편 로그인 이슈 해결
- [ ] 프로필 페이지 개선 및 기본 이미지 설정 완료 확인



> 이번 주는 “실사용자 입장에서 정말 편한 포카 거래란 무엇인가?”를 다시 묻는 과정, 단순한 CRUD 이상의 사용자 경험 설계가 핵심 과제임을 재확인. 
>
>다음 주에는 기술적 접근 방식(Python/OpenCV + 프론트엔드 UI 구조)과 UX 와이어프레임을 더 구체화할 계획