# 1. 제목

- 1~6개의 # 기호를 사용하여 제목 수준을 지정합니다. 

e.g.
# 제목
## 중제목
### 소제목

문서의 서식을 개개인이 지정하지 않고, 일관성을 유지하고자 markdown 을 통해 작성 - 표준화된 문서를 작성하고자

# 2. 텍스트 스타일
볼드, 이탈릭, 밑줄 처리 등
- 굵게: **단어**
- 기울기 : *단어*
- 취소 (삭제선) : ~~단어~~
- 굵고 기울게 : ***단어***

# 3. 텍스트 인용 

> 인용구문
> 여러줄도 사용 가능 (>) 을 통해서 

# 4. 코드 인용
(마크다운을 쓰는 핵심)

- 인라인 코드 인용 => 이것은 code 입니다. => `code` (숫자 1 옆 ` 백틱 으로 감싸주기기)

- 코드 블럭 : 백틱 세 번
```python (내가 사용하는 언어의 이름을 적으면, 색이 바뀜뀜)
def hello():
    print("hello!")
```

```javascript
console.log("hello")
```

# 5. 링크
- [내가 표시하고 싶은 이름](URL주소)

e.g. [구글](https://google.com)

# 6. 이미지

인터넷에서 사진을 불러 올 때
- ![사진에 대한 설명](보여주고 싶은 사진의 경로)
![희희희](https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzEyMTFfMjc1%2FMDAxNzAyMjg1ODAwMjA1.DIR9AyPCg9Fk1aWKRWe63gmvkVI8AlKW2zJ81zDeGQEg.AKmhGVzAeNzE4irQYVk6MDI6kDGatqng_UVwq5slXs8g.JPEG.cshop_hd_flagship%2F%25BF%25C0%25B9%25F6%25BB%25E7%25C0%25CC%25C1%25EE_%25B4%25EB%25B5%25CE_%25BE%25C8%25B0%25E6_%25C3%25DF%25C3%25B5__%25B8%25F0%25BD%25BA%25C4%25E0_%25B0%25A2%25C4%25C9%25BD%25BA_%2528feat._%25BA%25FC%25B4%25F5%25B3%25CA%25BD%25BA_%25B9%25AE%25BB%25F3%25C8%25C6_%25BE%25C8%25B0%25E6%252912.jpg&type=sc960_832)


- ![문땅훈](컴퓨터의 경로에 맞는 주소 넣기기)
e.g. -![문땅훈](../assets/cat.jpg)

.. 상대 경로 

# 7. 목록

##순서있는 목록
1. (한칸띄고) 첫번째
2. 두번째
3. 세번째

##순서없는 목록
- (한칸띄고) 첫번째
엔터 - 탭 해서 첫번째에 하위항목 생성 
e.g. 
    - 1-1
    - 1-2

- 두번째
- 세번째

e.g.
[대괄호 안에 X 적기] 는 체크박스를 만들어줌 (github에서)
- [X] TO-DO List (vscode에서는 안보이지만)

- terminal clear 하는 방법? 
: clear라고 쓰기 혹은 CTRL+L
- History 기능이 있으므로, 방향기 위 키로 내가 이전에 터미널에서 입력한 코드 불러올 수 있음. 

### Git에 업로드 하기 
`git init` 이라는 명령어로 .git 폴더를 만듦. 
`git add .` - add랑 . 은 띄어쓰기 해야함. (.은 현재 폴더를 의미함.) = ADD하고 COMMIT 할 것 이다. `git commit -m "내용" 
=> git config --global user.email "you@example.com" 으로 A uthor