# Javascript (JS)
> https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/What_is_JavaScript
>
: 기본예제 파일 다운로드 후 진행 

![JavaScript Wiki](/assets/js.png)

## JS의 특징
- 동적 언어
- 비동기
- 객체지향
- 호이스팅
- 타입이 없음
- 타입스크립트를 사용하면 타입이 존재함

- 움직임을 표현하기 위한 언어 
---
```
JavaScript is a high-level programming language that follows the ECMAScript standard.
```

- 브라우저를 조작하기위해서 만들어진 언어 (웹 브라우저의 css, html을 조작) -> Node js: 브라우저 조작, 서버 구축

![js 실행](/assets/js1.png)

----

# json placeholder
> https://jsonplaceholder.typicode.com/
가짜 백엔드 서버 
```
fetch('https://jsonplaceholder.typicode.com/todos/1')
      .then(response => response.json())
      .then(json => console.log(json))
```