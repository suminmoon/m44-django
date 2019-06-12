## DB Table을 추가하여 관계 형성하여 핸들링 하기

```bash
-app을 추가하지 않고 DB에 model 추가하여 사용해보자
DB에 model 추가하기 위해 models.py에 추가하고 makemigrations, migrate 하기
 
```



```bash
pip install django-extensions
=> 하면 shell_plus 사용 가능 
=> settings.py 에서 INSTALLED_APPS 이 부분에

    # 3rd party Apps
    'django_extensions',
    
- shell_plus
django 에 있는 model 들을 모두 import 한 상태로 사용할 수 있다.

    
```



#### Board에 댓글 다는 Comment 작성해보기

```bash
- 1:M 관계에 있는 데이터 핸들링 하기 (게시글:댓글)
- class Comment 와 class Board 사용

# 1. 특정 게시글 불러오기
board = Board.objects.get(pk=11)

# 2. 댓글 생성
comment = Comment()  # 인스턴스 생성
comment.content = '첫번째 댓글'  # 인스턴스변수 할당
comment.board = board
comment.save()

comment.id  # 1
comment.board  # <Board: 11. 수정합니다.>
comment.board_id  # 11
comment.board.id  # 11
comment.board.title  # 수정합니다.

# 3. 댓글 생성 2
board = Board.objects.get(pk=18)
comment = Comment()
comment.content = '두번째 댓글입니다.'
comment.board_id = board.id
comment.save()

comment.board  # <Board: 18. 새로운글>

# 4. 댓글 생성 3
comment = Comment(board_id=board.id, content='세번째 댓글입니다.')
comment.save()

# 5. 보드에서 댓글 가져오기
board = Board.objects.get(pk=11)
comments = board.comment_set.all()
comments  # <QuerySet [<Comment: <Board(11): Comment(1 - 첫번째 댓글입니다.)>>, <Comment: <Board(11): Comment(3 - 세번째 댓글입니다.)>>]>

```





```bash
- comment 추가하면서 id가 Board에도 있고 Comment에도 있기 때문에 명시적으로 board_id, comment_id로 표현하기
- 마찬가지로 views.py에 생성하는 함수의 이름도 comment_create식으로 명시하기

```



