# 명령어 정리 εïз

## `git init`
- 현재 디렉토리에 `.git` 폴더를 생성하여 새로운 Git 저장소를 초기화 한다.
    - 최초에 한번만 하면 된다. 선언하는 역할. 

## `git clone`
- 현재 디렉토리에 원격저장소 폴더를 복제.
    - pwd 를 통해 내가 있는 위치를 확인하고, 만일 이미 그 위치에 동일한 이름의 파일/ 폴더가 있다면, 에러가 발생함. 
    
    -  git clone https://github.com/iam-Aerin/TIL.git (새로운 이름)


```
git clone {remote_url}
git clone {remote_url} {directory_name}
```
## `git status`
- 현재 git의 상태를 확인하는 명령어
    - tracked, untracked 파일을 구분하여 표시해줌. 

## `git add`
- working directory 에서 변경된 파일을 staging area에 이동. 

```
git add . (.은 내가 올리고 싶은 파일 혹은 폴더의 이름을 뜻한다.)
```

```
git add {file_name/directory_name}
git add . => 현재 나의 위치를 기준으로 모든 파일과 폴더를 의미한다. 
```

## `git commit`
- staging area에 있는 변경사항`을 커밋하여 스냅샹을 생성하는 것. 

## `git log`
- 커밋의 히스토리를 조회
- 사진들의 목록을 보는 명령어
    - option
        - `--oneline`: 한눈에 보기 좋게 결과를 불러옴.
        - `--graph` : 커밋들에 하나하나의 선을 달아서 보여줌. - 흐름을 보기 좋게 보여줌. 

## `git remote`
- 원격저장소 관리 명령어
(`git remote -v` 로는 더 자세한 url 정보까지 확인 가능함.)

- 원격 저장소 추가
    - 일반적으로 remote_name은 `origin` 사용
 ```
git remote add {remote_name} {remote url}
```
    - git remote add <단축이름> <url> 명령을 사용한다.

- 원격 저장소 삭제

```
git remote remove
```