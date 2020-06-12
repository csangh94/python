from django.contrib.auth.models import User
from django.db import models

class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_photos')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d',default='photos/no_image.png')
    created = models.DateTimeField(auto_now_add=True)  # 등 록 할 때 시간 등록
    updated = models.DateTimeField(auto_now=True)      # 수  정  할 ㄸ ㅐ 시간 수정
    text = models.TextField(default='')
    class Meta:
        # ordering = ['updated']  # 오름차순
        ordering = ['-updated']   # 내림차순

    def __str__(self):
        return self.author.username+" " + self.created.strftime('%Y-%m-%d %H:%M:%S')
