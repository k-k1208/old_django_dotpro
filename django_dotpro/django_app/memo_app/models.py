from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


class Memo(models.Model):
    content = models.CharField(max_length=2000)
    update_datetime = models.DateTimeField(auto_now_add=True) #モデルを追加した日時を記録
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    #ForeignKeyは多対一のモデルを作る時に使う。たとえばツイッターのユーザー(1)とツイート(多数)関係
    #多側に外部キーを設ける(主キーと外部キーがあるgit add .子テーブル) ,１側は主キーのみの親テーブル
    #get_user_modelはdjango上で有効になっているユーザーモデルを所得。
    #on_deleteは参照するオブジェクトが削除された時に、それと紐づけられたオブジェクトも一緒に削除するのか、それともそのオブジェクトは残しておくのか(SET_NULL)を設定する
    #SET_NULLはオブジェクトが削除されると代わりにNULLをセットする。そのためにnull=Trueとする必要がある。
    #null=Trueは空欄を許容する。

    #　__str__(self)はオブジェクトを文字列に変換して返す
    def __str__(self):#? これが何かわかっていない
        return 'id=' + str(self.id) + 'update_datetime=' + str(self.update_datetime)