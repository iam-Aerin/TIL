DAMF2  에서 다른 사람의 코드/ 파일 clone  하기
git bash
git clone <git url>

=> 이후 vscode로 열고 기본 설정하는 방법
: python -m venv venv 
가상 환경 활성화

source venv/Scripts/activate

pip install <django>

git ignore하는 것들이 있다면 추가해주시 
> e.g. venv <가상환경>
> migrations 은 안해도되나, (만약 있다면) `migrate` 해야함. 
