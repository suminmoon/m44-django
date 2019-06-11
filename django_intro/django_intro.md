# Web Application (django)

- Dynamic web
- 프레임워크 사용

### Django - How?

``` :bash
-M(model) : 데이터를 관리
-T(Template) : 사용자가 보는 화면 (html)
-V(View) : 사용자의 요청의 오는곳
```



--- django 프로젝트를 생성하면 반드시 실행해야 하는 과정 ---

```
1. pip install django
(장고 설치)
2. django-admin startproject crud .
(현재 디렉토리에서 프로젝트 시작하겠다)
3. python manage.py startapp boards
(app 생성)
--
4. settings.py에서
INSTALLED_APPS 에 
 '(app이름).(apps).(apps.py의 class 이름)'  
 # = 'boards' '앱이름'으로만 적어도 된다
( ) 은 제거

LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
```



1. 장고 시작하기

```bash
$ django-admin startproject intro . # 현재 디렉토리에 intro라는 이름으로 장고를 시작해라
$ python manage.py runserver  # 서버 실행
```

2. 장고 파일 의미

```bash
urls.py : url 연결 ( 요청을 확인하고 요청이 어디로 가야하는지 / views로 넘겨줌)
wsgi.py : 배포에 필요
db.sqlite3 : 데이터베이스
---------
pages app 만들고
---------
admin.py : 관리자 페이지
apps.py : app의 정보가 담김
models.py : 데이터베이스 혹은 앱에서 사용되는 모델들이 정의되는 곳
test.py : test 코드 작성
views.py : cotroller와 같은 곳. 뭔가 구현?
```

3. app 생성

```bash
$ python manage.py startapp pages  # pages라는 app 생성
```

4. setting.py에 app 등록 (우리가 만든 app을 반드시 등록 해야함)

```bash
INSTALLED_APPS = [

	# 추가        # apps.py에 있는 class 이름
    'pages.apps.PagesConfig',  
    
--

LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'

```



---



1. urls.py

2. views.py

3. templates 디렉토리 만들고 여기에 views.py 에서 요청하는 html 파일 넣기



- 변수 routing

```bash
<views.py>
def greeting(request, name):
    return render(request,'greeting.html', {'name': name})

<urls.py>
path('greeting/<str:name>/', views.greeting),
```



#### html 파일에 여러가지 기능 추가 ( for문, if문 등)





#### 사용자에게 입력 받는 것 (요청받아 처리하기 throw/ catch) form 태그

- throw   =>

- catch    =>

```bash
<views.py>

def throw(request):
    return render(request, 'throw.html')


def catch(request):
    message = request.GET.get('message')
    message2 = request.GET.get('message2')
    context = {'message': message, 'message2': message2}
    return render(request, 'catch.html', context)


<throw.html>
<form action="/catch/">
        던질 거 : <input type="text" name = "message">
        하나 더 : <input type="text" name = "message2">
        <input type="submit">
    </form>
<catch.html>
    <h1>Catch page</h1>
    <p>첫번 째 메세지: {{ message }}</p>
    <p>두번 째 메세지: {{ message2 }}</p> 
```

- request : 사용자가 input으로 보낸 정보를 담고 있으며, 꺼내서 사용할 수 있다.



---

#### css 파일 만들어서 디자인 입히기					

```bash
static 디렉토리 만들어서 관리
static/stylesheets/style.css
static/images/image.jpg
```

```
<static_example.html>

{% load static%}

 <!DOCTYPE html>
 <html lang="en">
 <head>
     <meta charset="UTF-8">
     <title>static_example</title>
     <link rel="stylesheet" href="{% static 'stylesheets/style.css' %}" type="text/css">
 </head>
 <body>
     <h1>Static example</h1>
     <img src="{% static 'images/image.jpg' %}" alt="BTS">
 </body>
 </html>
```



setting.py 에서 

```
INSTALLED_APPS = [ ]

여기에 등록한 순서대로 찾아가면서 실행되기 때문에 서로 다른 app에 같은 html 이름이 있으면 
다른 것이 실행될 수 있기 때문에 templates에 디렉토리(app 이름) 만들어서 안에 관리하기

```
```buildoutcfg
여러 app이 있을 때 장고는 templates/static들을 한 곳에 모아서 관리하기 때문에  같은 이름의 html 있을 경우 내가 원하지 않는 html을 불러올 수 있다.
-> templates 내에 app 이름으로 디렉토리를 만들고 그 속에 html 파일을 넣아야 한다.
```

---

#### ~장고 Web 구성 계속

- html 상속 받기 
```buildoutcfg
{% extends 'utilities/base.html' %}
-> 앱 안에 있는 template 폴더 찾음

{% block body %}
 ~ 내용 ~
{% endblock %}

=> web 서버 결과
Utilities
welcome to utilities page
Copyright 2019

index.html 내용은 base.html의 
section 부분에 표현된다.

<base.html> 에서
       <section>
            {% block body %}
            {% endblock %}
        </section>
        
<index.html>
{% block body%}
    <h2>Welcome to utilities page</h2>
{% endblock %}

```

```buildoutcfg
상속 받을 때 html 작성 시 상속 구문인 
{% extends 'utilities/base.html' %}와 같은 구문을 가장 위에 명시 해야한다.

```

{% load static %}
-> static 폴더에 있는 이미지나 css 사용할 때

---

-settings.py 수정
```buildoutcfg
TEMPLATES = [
    {
        'DIRS': [os.path.join(BASE_DIR, 'intro', 'templates')],
     } 
 이부분 추가하기 
    => 어떤 app에서든 'base.html' 상속받아 사용할 수 있게 된다.
       
```

