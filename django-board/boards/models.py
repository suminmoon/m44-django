from django.db import models
from imagekit.models import ProcessedImageField  # new
from imagekit.processors import Thumbnail  # new

# Create your models here.


class Board(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    # image = models.ImageField(blank=True)
    image = ProcessedImageField(
        upload_to='boards/images',  # 저장 위치 설정 ( media 이후의 경로 설정 )
        processors=[Thumbnail(200, 300)],
        format='JPEG',
        options={'quality': 90},
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # admin 페이지에 데이터 보여지는 형태 지정
    def __str__(self):
        return f'{self.id}. {self.title}'
    

# 새로운 app 을 생성하지 않고 class 를 추가하여 board 의 DB 에 추가?
class Comment(models.Model):
    content = models.TextField()  # 댓글의 내용
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        return f'<Board({self.board_id}): Comment({self.id} - {self.content})>'
