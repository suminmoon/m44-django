from django.db import models

# Create your models here.


class Board(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
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