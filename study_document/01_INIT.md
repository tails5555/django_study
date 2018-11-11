# Initialize Project

django 프로젝트를 처음 진행하기 위한 토막 문서입니다.

아래 문서를 참고하셔서 이를 이용한 프로젝트를 진행하시면 도움 될 것입니다.

## Before Tutorial

Python 3 버전을 기준으로 django 프레임워크를 우선 설치하셔야 합니다. 이전에 pip 버전이 최신 버전인지 확인하시고 설치하고 진행하시길 바랍니다.

우선 MVC 패턴을 이용한 Web Application 을 만드기 위한 설치 항목은 django 만으로 충분합니다. 

나중에 JavaScript Web Application 과 연동하여 데이터를 주고 받는 RESTful API 구축을 원하면 아래 설치 항목도 같이 추가 하시길 바랍니다.

RESTful API 구축을 이용한 연동 과정은 차후에 진행 하겠습니다.

```
pip install django
pip install django-rest-framework
```

## First Project Initialize

django 프레임워크를 이용해서 프로젝트를 생성하는 문장은 다음과 같습니다. 밑줄 친 부분에는 프로젝트 자체의 이름을 입력하시면 됩니다.

```
django-admin startproject ______
``` 

참고로 본인은 프로젝트 초반의 이름을 django_hello 로 설정하였습니다.

초반 프로젝트의 구성은 아래와 같습니다.

```
django_hello/ -- 이건 솔직히 이름에 큰 영향은 없습니다.
    manage.py
    django_hello/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```

이를 토대로 django 프로젝트가 어떻게 구성 되는지 자세히 알아보도록 합니다.

- manage.py 

    Django 프로젝트와 상호작용을 위한 커멘드 라인 유틸리티 입니다. Spring 으로 치면 Application.java 파일과 같은 역할을 합니다. 
    
    아래와 같은 명령어를 이제 밥 먹듯이 진행하게 되니 이 파일이 존재하는 디렉토리를 숙지해 두시길 바랍니다.

    ```
    python manage.py runserver
    python manage.py makemigrations
    python manage.py migrate
    python manage.py startapp _______
    ```

- 하위 django_hello/ 

    이 내부에는 project 를 위한 Python 패키지들이 저장이 됩니다. 처음 django 프로젝트를 생성할 때 만든 django_hello 디렉토리가 이를 관리하는 디렉토리입니다. 이 내부에 있는 py 파일의 역할은 아래와 같이 참고할 수 있습니다.

- \_\_init\_\_.py

    이것이 폴더 안에 있다는 의미가 **이 폴더는 Python 의 패키지 입니다** 라는 푯말과 같습니다.

- settings.py

    django 프로젝트의 설정을 관리하는 파일입니다. django 프로젝트에서 사용할 패키지를 추가할 때, 초기화 시간인 미국 시간에서 한국 시간으로 변경할 때 등 사용하는 경우도 더러 있습니다.

- urls.py

    django 의 URL 목록들을 저장하는 파일입니다. URL 에서는 Path Variable 방식의 전달과 일반적인 URL 로 전달하는 방식, kwargs 변수를 이용한 임의의 값 전달 등을 적용할 수 있습니다.

- django_hello/wsgi.py

    WSGI(Web Server Gateway Interface) 를 호환하기 위한 웹 서비스의 진입점입니다. django 프로젝트는 JSP, Spring 프로젝트(WAS 호환) 와 달리 WSGI 로 제공을 하는 것이 관례입니다.

    WSGI 는 Application 과 Server 양단으로 나뉘어져 있어 Server 측에서 환경 정보, 콜백 함수 등을 Application 측에 제공해야 하는 원칙입니다. 혹은 Middleware 라고 칭합니다.

    WAS 와 WSGI 의 차이에 대해서는 후술하겠습니다.

## `settings.py` Structure

django 프로젝트의 Main Project 인 django_hello 디렉토리에 `settings.py` 파일을 실행하면 Web Application 을 실행할 때 필요한 설정 키워드들이 들어 있습니다.

개략적으로 어떤 개념들이 있는지 알아두고 넘어 가겠습니다.

- `LANGUAGE_CODE`
  
    django 프로젝트 admin 페이지에 대한 언어 설정할 때 필요한 키워드입니다.

- `TIME_ZONE`
    
    django 프로젝트의 시간대를 설정합니다. 해당 시간대 설정은 나라 별로 다르니 맞춰서 설정하셔야 됩니다.

- `STATIC_URL`, `STATIC_ROOT`

    Web Application 을 실행할 때, JavaScript, CSS, Sass 파일 등을 가져오는 주소 설정하는 요소입니다. URL 만 설정하면 각 Application 별로 같은 위치로 설정되고, ROOT 위치까지 설정하면 모든 Application 에서 같은 위치로 접근 가능하도록 합니다.

- `MEDIA_URL`, `MEDIA_ROOT`
    
    데이터베이스를 이용한 파일 업로드를 진행하는 과정 중 이 데이터에 대한 저장 주소를 설정하는 요소입니다. Media 파일은 이미지 파일, 문서 파일 등을 올릴 수 있고, static 설정과 같은 맥락으로 이해하실 수 있습니다.

- `ALLOWED_HOSTS`
    
    RESTful API 를 구축하거나 접근 가능한 Host 주소만 설정할 때 사용합니다. 이는 Cross Origin 에 대한 설정과 유사합니다.

- `DATABASES`

    데이터베이스에 대한 설정입니다. 기본 SQL 드라이버는 SQLite3 을 이용합니다. MySQL, MariaDB, Redis, MongoDB 등 다른 데이터베이스를 사용하기 위한 설정은 차후에 다뤄 보겠습니다.

- `INSTALLED_APPS`    

    이 Web Application 을 실행하기 위한 모든 의존성 모듈 패키지를 작성합니다. 각 Gateway 별 Application 모듈 패키지를 Web Application 에서 이용하기 위해 다음과 같이 추가하시면 됩니다.

    ```
    [ ..., '[APP이름].apps.[AppConfig]' ]
    ``` 

## Module Application Initialize

Main Application 에 대한 혼동을 방지하기 위하여 데이터베이스를 다루는 Application 을 Module Application 으로 호칭하겠습니다.

이를 생성하기 위해 Main Application 디렉토리에 있는 `manage.py` 를 이용하시길 바랍니다. 

아래 문장에 있는 빈 칸은 원하는 Module Application 이름을 작성하시면 됩니다. 

```
python manage.py startapp ________
```

그리고 `models.py` 를 이용하여 데이터베이스를 구성하고, Web Application 에 동봉된 데이터베이스로 마이그레이션을 진행하셔야 합니다.

Model 구성하는 방법은 다음 장에서 다루겠습니다.

# Author

- 강인성([tails5555](https://github.com/tails5555))