from django.urls import path
from . import views #? 同じ階層にあるviews.pyファイルをインポートしています。ドットは、同じ階層という意味(カレントディレクトリ)

urlpatterns = [
    path('', views.index, name='index'), # urlに何もない時は、view.pyのindex関数を呼び出すという意味になる。
    path('<int:now_page>', views.index, name='index'),#<変数>とroute部分に記述することで、views内にurlから変数を渡すことができる
    path('post', views.post, name='post'),
    path('set_record_number', views.set_record_number, name='set_record_number'),
    path('set_order_option', views.set_order_option, name='set_order_option')
]