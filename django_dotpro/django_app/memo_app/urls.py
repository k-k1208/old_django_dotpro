from django.urls import path
from . import views #? 同じ階層にあるviews.pyファイルをインポートしています。ドットは、同じ階層という意味(カレントディレクトリ)

urlpatterns = [
    path('', views.index, name='index'), #? urlに何もない時は、view.pyのindex関数を呼び出すという意味になる
    path('post', views.post, name='post'),
]