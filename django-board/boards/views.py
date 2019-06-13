from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from .models import Board, Comment
# Create your views here.


@require_http_methods(['GET'])
def index(request):
    # Board 의 전체 데이터를 불러온다 - QuerySet (list와 유사한 형태지만 실제 list는 아님)
    boards = Board.objects.all()
    context = {'boards': boards}
    return render(request, 'boards/index.html', context)


# 사용장 입력을 받는 페이지 렌더링
@require_http_methods(['GET', 'POST'])
def new(request):
    # GET
    # POST
    # print(request.method) => GET
    if request.method == 'GET':
        return render(request, 'boards/new.html')
    else:
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')    # 사용자로 부터 받는 데이터의 종류가 파일 이미지이다.
        board = Board(title=title, content=content, image=image)
        board.save()
        return redirect('boards:detail', board.id)



# 데이터를 받아서 실제 DB에 작성
# def create(request):
#     title = request.POST.get('title')
#     content = request.POST.get('content')
#     board = Board(title=title, content=content)
#     board.save()
#
#     return redirect('boards:detail', board.id)   # 새로운 글을 작성해서 제출 누르면 바로 상세 페이지로 연결


# 특정 게시글 하나만 가지고 오기
# localhost:8000/boards/<id>/
@require_http_methods(['GET'])
def detail(request, board_id):
    # Board 클래스를 사용해서 id 값에 맞는 데이터를 가지고 온다.
    # context 로 넘겨서 detail.html 페이지에서 title 과 context를 출력해본다.

    # board = Board.objects.get(id=id)   # get => 특정 id 값으로 접근 (주로 pk 같이 유일한 값)
    board = get_object_or_404(Board, id=board_id)
    comments = board.comment_set.order_by('-id').all()
    context = {'board': board, 'comments':comments}
    return render(request, 'boards/detail.html', context)


@require_http_methods(['POST'])  # POST 로 들어올 때만 로직이 돌고 아니면 에러 발생. 그래서 if 문 안 써도 된당
def delete(request, board_id):
    # GET 요청으로 들어오면 detail page 로 다시 redirect
    # POST 요청으로 들어오면 정상 삭제

    # if request.method == 'GET':
    #     return redirect('boards:detail', id)
    #
#    else:
        board = Board.objects.get(id=board_id)
        board.delete()
        return redirect('boards:index')


# 게시글 수정 페이지 렌더링
@require_http_methods(['GET', 'POST'])
def edit(request, board_id):
    # GET
    # POST
    # board = Board.objects.get(id=id)  # 아래 if 문과 else 문에 중복되기 때문에 밖으로 꺼내서 한 번만 처리하기 Don't Repeat Yourself
    board = get_object_or_404(Board, id=board_id)
    # 1. 사용자의 요청이 GET인지 POST 인지 확인
    if request.method =='GET':
        # 2. GET 요청이면 사용자에게 수정할 페이지 보여준다.
        context = {'board': board}
        return render(request, 'boards/edit.html', context)
    else:
        # 3. POST 요청이면 사용자가 보낸 데이터를 받아서 수정한 뒤 detail page 로 redirect 한다.
        title = request.POST.get('title')
        content = request.POST.get('content')  # 사용자가 보낸 title 과 content 받기
        image = request.FILES.get('image')  # new
        # 수정 로직
        board.title = title
        board.content = content
        board.image = image
        board.save()
        return redirect('boards:detail', board_id)  # f'/boards/{id}/' 이거를 이름 지정한 걸로 바꾸기


# def update(request, id):
#     # id 값에 맞는 board 데이터를 위에서 주어진 title 과 content 에 맞게
#     # 수정한 뒤 저장하는 로직
#     title  = request.POST.get('title')
#     content = request.POST.get('content')  # 사용자가 보낸 title과 content 받기
#     # id 값에 맞는 데이터 가져오기
#     board = Board.objects.get(id=id)
#     # 2. 해당 데이터의 내용을 주어진 title, content 로 지정
#
#     board.title = title
#     board.content = content
#     # 3. 저장
#     board.save()
#     return redirect('boards:detail', id)  # f'/boards/{id}/' 이거를 이름 지정한 걸로 바꾸기


def comment_create(request, board_id):
    # 댓글 생성하는 로직
    content = request.POST.get('content')
    comment = Comment()
    comment.board_id = board_id
    comment.content = content
    comment.save()

    return redirect('boards:detail', board_id)


@require_POST
def comment_delete(request, board_id, comment_id):
    # 댓글 삭제 로직
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect('boards:detail', board_id)
