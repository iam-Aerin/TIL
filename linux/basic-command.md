# Linux 기본 명령어

## 0. 명령어의 기본형식
```
command [options] [arguments]
```

보통 실행하고 싶은 프로그램의 이름을 맨 앞에 적는다. 
e.g. python -V -> 띄어쓰기를 기준으로 하기 때문에, 꼭 띄어쓰기에 유의해야함. 

보통 options 의 앞에는 - 가 들어간다. 

- command : 실행할 명령어, 프로그램
- options : 명령어의 옵션
- arguments : 명령어에 전달할 값 (데이터)

## 1. 파일 및 디렉토리 관리

### ls 는 list 의 약자로, 현재 내가 있는 위치의 모든 폴더를 보여주세요. 라는 역할

- 디렉토리 내용 목록을 보여줍니다. 
- options: 
    - `-l` : 파일의 상세 정보 표시
    - `-a` : 숨김 파일 표시시

. 은 현재 폴더, ..은 상위 폴더를 나타낸다. 

### cd (change directory)

- 현재 작업 디렉토리를 변경합니다. 
- `cd {target-directory}`
    - target-directory는 자동완성 기능 (Tab) 키를 이용
    - pwd (print working directory): 현재 작업 중인 디렉토리의 전체 경로를 출력 (내가 어디에 있는지 위치를 표시하기 위해 - 보통 mac에서 현위치가 파악이 안될때 pwd를 입력하여 파악할 수 있음.)

    ### mkdir (make directory)
    - 새로운 디렉토리를 생성하는 명령어
    - `mkdir {directory-name}`
    e.g. mkdir markup => 을 터미널에 입력해해서 TIL 폴더안에 markup 이라는 폴더를 생성

    ### touch 
    - 새로운 파일을 생성
    - `touch {file-name}`

    ### rm (remove)
    - 파일이나 폴더를 삭제. 
    - options
        - 파일은 지울 수 있으나, 폴더 (directory) 를 지울 수 없다. 하여, rm 후에 `-r`이라는 옵션을 추가해줘야함.
        - `-r` : 디렉토리와 그 내용용을 재귀적으로 삭제

    ### cat (concatenate)
    ; 연결하다, 사슬
    