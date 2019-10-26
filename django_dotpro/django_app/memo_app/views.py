from django.shortcuts import render, redirect
from django.views.generic import TemplateView#class_based_view　汎用ビュー

from .models import *

from .forms import PostForm


# Create your views here.

def index(request):
    memos = Memo.objects.all()
    params = {
        'memos': memos,
        'form': PostForm() #これが抜けていたためテキストエリアが表示されへんかった
      }
    return render(request, 'index.html', params)#renderメソッドの第三引数に変数(辞書型)を入れることで、templateのhtmlファイルに使う変数を渡せる、辞書に使う変数を全部格納してしまう


def post(request):
    form = PostForm(request.POST, instance=Memo())
    if form.is_valid(): #validateで検証という英単語だから、formの内容が有効かどうかを観察するためのis_valid
        form.save() #formの保存
    else:
        print(form.errors)

    return redirect(to='/')

