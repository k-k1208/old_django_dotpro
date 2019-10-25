from django.db import models

# Create your models here.


class Memo(models.Model):
    content = models.CharField(max_length=2000)
    update_datetime = models.DateTimeField(auto_now_add=True) #モデルを追加した日時を記録


    #　__str__(self)はオブジェクトを文字列に変換して返す
    def __str__(self):#? これが何かわかっていない
        return 'id=' + str(self.id) + 'update_datetime=' + str(self.update_datetime)