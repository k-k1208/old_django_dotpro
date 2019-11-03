from django.shortcuts import render, redirect
from django.views.generic import TemplateView#class_based_view　汎用ビュー

from .models import *

from .forms import PostForm, RecordNumberForm
from django.core.paginator import Paginator


# Create your views here.

def index(request, now_page=1):

    print("===========1")#テスト用
    print(request.POST)#テスト用
    #フォームで撮ってきたrecordnumberを変数として格納して、paginatorに入れましょう
    if 'record_number' in request.POST:
        print("=============2")#テスト用
        print(request.POST)#テスト用
        record_number = request.POST['record_number']#結局ポストは辞書型を指している。でここではRecordNumberFormのchoiceの辞書型を指している。
    else:#リクエストがないデフォルトの表示件数を10件にする。
        record_number = 10

    record_number_form = RecordNumberForm()#RecordNumberFormのインスタンス化
    record_number_form.initial = {'record_number': str(record_number)}#初期値(開いた時に件数として表示されるやつの設定)

    memos = Memo.objects.all().order_by('update_datetime').reverse()
    page = Paginator(memos, record_number)
    params = {
        'page': page.get_page(now_page),#指定されたページにあるオブジェクトをとってくる。
        'form': PostForm(),#これが抜けていたためテキストエリアが表示されへんかった
        'record_number_form': record_number_form,
    }
    return render(request, 'index.html', params)#renderメソッドの第三引数に変数(辞書型)を入れることで、templateのhtmlファイルに使う変数を渡せる、辞書に使う変数を全部格納してしまう


def post(request):
    form = PostForm(request.POST, instance=Memo())
    if form.is_valid(): #validateで検証という英単語だから、formの内容が有効かどうかを観察するためのis_valid
        form.save() #formの保存
    else:
        print(form.errors)

    return redirect(to='/')

