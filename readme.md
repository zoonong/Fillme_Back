## 프로젝트 실행 방법(순서대로 진행하기)

### 1. 레퍼지토리 클론
    git clone https://github.com/OIDC-JT/NBP_back.git

### 2. 가상환경 실행
    source myvenv/Scripts/activate

### 3-a. 라이브러리 설치
    pip install -r requirements.txt

### 3-b. reqirements.txt로 필요한 라이브러리 설치가 안된다면
    pip install django
    pip install djangorestframework
    pip install django-cors-headers
    pip install djangorestframework-simplejwt
    pip install dj-rest-auth

### 4. 프로젝트 폴더 위치로 이동 (manage.py 파일이 있는 위치)
    cd cloud

### 5. DB 마이그레이션
    python manage.py makemigrations
    python manage.py migrate

### 6. 서버 실행
    python manage.py runserver

## API

### 유저 회원가입 및 로그인/로그아웃

### 회원가입 및 자빅스 db 자동 생성
### 127.0.0.1:8000/accounts - POST 메소드 사용
    username, email, password1(비밀번호), password2(비밀번호 확인) 입력
    ex)
    {
        "username" : "유저네임 입력",
        "email" : "이메일형식 입력",
        "password1" : "비밀번호",
        "password2" : "비밀번호 확인"
    }

### 로그인
### 127.0.0.1:8000/accounts/login - POST 메소드 사용
    username, password 입력
    ex)
    {
        "username" : "유저네임",
        "password" : "비밀번호"
    }

### 로그아웃
### 127.0.0.1:8000/accounts/logout - POST 메소드 사용
    입력값 없이 POST방식으로 보내기