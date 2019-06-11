- crud : 프로젝트 명 / boards : app 명

- app내에 urls.py 파일 생성하기 => 프로젝트 urls 에 경로 지정 후 생성

- base.html이라는 기본 템플릿 만들어서 board의 html들이 base를 상속받아 사용하도록 설정
 bit.do/m44-docs => share > base.html
 
 #### 요청을 GET 으로 하는 것과 POST 로 하는 것의 차이는?
 ```bash
 - 서버에 무언가를 전달할 때 사용하는 방식
 - GET 은 주소줄에 ?값 뒤에 쌍으로 이어붙고 POST 는 숨겨진다.
 - GET은 가져오는 것이고, POST 는 수행하는 것이다.
 - GET은 select 적인 성향, 서버의 값이나 상태 등을 바꾸지 않음
 - POST 는 서버의 값이나 상태 등을 바꾸기 위해 사용
 
 ```
 
 ```bash
  - new.html 의 method = "post"  / post로 요청
    => ~ 를 주세요 를 ~ 를 해주세요. 의 의미 
     title = request.GET.get('title')
     content = request.GET.get('content') 
    => 이거 post 요청으로 바꿔야함
    
  - render => html을 바로 서빙 해주겠다.
  => post 는 index 페이지(여기서는 /boards/)로 이동 시켜주겠다. 로 바꿔야함
  => 사용자를 index 페이지로 연결 시켜줄 수 있는 redirect 
  => 모든 작성이 끝나면 index 페이지로 redirect
 ```
 
 
 - 게시판의 detail page 로 들어가기 (특정 게시글 하나만 가지고 오기) 
 ```bash

 path('<int:id>/', views.detail)
 
 def detail(request, id):
    
    board = Board.objects.get(id=id)  # 특정 id 값으로 접근
    context = {'board': board}
    return render(request, 'boards/detail.html', context)

 
 ```
 
 - 게시글 올리고 제출하면 바로 상세 페이지로 연결
```bash

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    print(request.GET)
    board = Board(title=title, content=content)
    board.save()

    return redirect(f'/boards/{board.id}/')   
    # 새로운 글을 작성해서 제출 누르면 바로 상세 페이지로 연결
                    # localhost:8000/boards/6 여기
``` 



- 게시글 삭제하기 (Delete)
```bash
board = Board.objects.get(id=id)
board.delete

<urls.py>
 path('<int:id>/delete/', views.delete),
 
<views.py>
 def delete(request, id):
    board = Board.objects.get(id=id)
    board.delete()
    return redirect('/boards/')


<detail.html>
<a href="/boards/{{board.id}}/delete">[삭제하기]</a>

```

--- 위 작업을 POST 요청으로 바꿔보자! ---
=> csrf 토큰을 이용하여 보완 강화 (수정, 등록, 삭제 등 DB를 조작할 때)

```bash
    <form action="/boards/{{board.id}}/delete/" method="post">
            {% csrf_token %}  # 보완 강화!!!!
        <input class="btn" type="submit" value="삭제하기" />
    </form>

```


- Update
```bash
boards/id/edit 들어가면 id의 데이터들이 들어가있게 만들기
value로 초기값 지정할 수 있다.
<input name ="title" id="title" type="text" value="{{ board.title }}"/><br />

textareasms 이런 식으로 넣기
<textarea name="content" id="content">{{ board.contet}}</textarea><br />

1. Board 클래스를 통해 id 값에 맞는 데이터를 가져온다.
2. 해당 데이터의 내용을 주어진 title, content 로 수정한다.
3. 저장한다.
-
```




- 페이지 이름을 명시적으로 지정해서 이름으로 접근하기

```bash

<urls.py>
app_name = 'boards' 맨 위에 추가 

< views.py 의 함수들 중 redirect로 경로 잡아놓은 부분 변경 >
return redirect('boards:detail', id)
=> detail이라는 이름을 가진 path('<int:id>/', views.detail, name='detail') 이 경로


<index.html의 경로들 변경 -> id값 들어가는 것들 뒤에 꼭 붙여주기>
<a href="/boards/{{ board.id}}>"
=> <a href="{% url 'boards:detail' board.id %}">[상세글 보러가기]</a>
<a href="/boards/new/">
=> <a href="{% url 'boards:new' %}">새로운 글 작성하러 가기</a>
 이런식으로 모든 html 변경해줘야함
```



- 코드를 RESTful 하게 작성해보기
```bash
1. new 와 create 둘 다 새로 생성하겠다는 의미기 때문에 두 개로 나눠질 필요가 없다.
=> 새롭게 생성하겠다 라는 로직을 하나로 묶고 두 가지 method(GET과 POST) 로 분기
=> GET 으로 들어오면 작성할 페이지를 보여주기, POST로 들어오면 작성하겠다.

request.method 가 'GET'이면 사용자 입력 받는 페이지 렌더링
request.method 가 'POST'면 데이터를 받아서 실제 DB에 작성하기

def new(request) 하나로 new 와 create 로직 수행

---

위와 마찬가지로 edit과 update 를 하나의 로직으로 합치기
def edit(request, id) 로 edit 로직과 update 로직 수행

GET    /boards/<id>/edit
POST   /boards/<id>/update
```