# Git 기본 개념 ꯁ

## 분산 버전 관리 시스템
- 클라이언트 (내 컴퓨터) 와 서버 (Git Hub) 모두가 똑같은 데이터를 유지하여 버전을 관리하는 시스템

## Git  파일의 세가지 상태 

![areas](../assets/areas.png)

- https://git-scm.com/book/ko/v2/%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0-Git-%EA%B8%B0%EC%B4%88

- 영역
    - working directory : 작업 영역 (작성하고 있는 코드, 모든 파일을 의미함.)
    - staging area : add 명령어로 무대 위로 올라간 파일들
    - .git directory (repository) : commit 명령어로 찍힌 스냅샷들을 저장

   ** => **add를 안하고, commit을 하는 실수가 종종 발생함 !****


   ## 파일의 라이프 사이클w
   ![lifecycle](../assets/lifecycle.png)
   
   - 워킹 디렉토리의 모든 파일은 크게 **Tracked(관리대상임)와 Untracked(관리대상이 아님)로 나눈다.** 
   
        - Tracked 파일은 이미 스냅샷에 포함돼 있던 파일이다. Tracked 파일은 또 Unmodified(수정하지 않음)와 Modified(수정함) 그리고 Staged(커밋으로 저장소에 기록할) 상태 중 하나이다. 간단히 말하자면 Git이 알고 있는 파일이라는 것이다.

        - 그리고 나머지 파일은 모두 Untracked 파일이다.

        - 마지막 커밋 이후 아직 아무것도 수정하지 않은 상태에서 어떤 파일을 수정하면 Git은 그 파일을 Modified 상태로 인식한다. 실제로 커밋을 하기 위해서는 이 수정한 파일을 Staged 상태로 만들고, Staged 상태의 파일을 커밋한다. 
        
    이런 라이프사이클을 계속 반복한다.