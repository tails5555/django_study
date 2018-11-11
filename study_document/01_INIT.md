# Initialize Project

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

- __init__.py
- 
    이것이 폴더 안에 있다는 의미가 **이 폴더는 Python 의 패키지 입니다** 라는 푯말과 같습니다.

- settings.py

    django 프로젝트의 설정을 관리하는 파일입니다. django 프로젝트에서 사용할 패키지를 추가할 때, 초기화 시간인 미국 시간에서 한국 시간으로 변경할 때 등 사용하는 경우도 더러 있습니다.

- urls.py

    django 의 URL 목록들을 저장하는 파일입니다. URL 에서는 Path Variable 방식의 전달과 일반적인 URL 로 전달하는 방식, kwargs 변수를 이용한 임의의 값 전달 등을 적용할 수 있습니다.

- django_hello/wsgi.py

    WSGI(Web Server Gateway Interface) 를 호환하기 위한 웹 서비스의 진입점입니다. django 프로젝트는 JSP, Spring 프로젝트(WAS 호환) 와 달리 WSGI 로 제공을 하는 것이 관례입니다.

    WSGI 는 Application 과 Server 양단으로 나뉘어져 있어 Server 측에서 환경 정보, 콜백 함수 등을 Application 측에 제공해야 하는 원칙입니다. 혹은 Middleware 라고 칭합니다.

    WAS 와 WSGI 의 차이에 대해서는 후술하겠습니다.
    

    