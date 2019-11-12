from django.shortcuts import render, redirect
from django.views.generic import TemplateView#class_based_view　汎用ビュー

from .models import *

from .forms import PostForm, RecordNumberForm, SetRecordForm
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model#ユーザーごとの表示のため　Memo.object.all()~~も全てMemo.objects.filter(user=request.user)に帰る

# Create your views here.

def set_record_number(request):
    request.session['record_number'] = request.POST['record_number']
    return redirect(to='/')

def set_order_option(request):#formで作られたプルダウンフィールドをセッション格納処理する関数。POSTをSESSIONに格納
    request.session['record_order'] = request.POST['record_order']
    return redirect('/')


def index(request, now_page=1):

#表示件数の部分
    if 'record_number' in request.session:
        record_number = request.session['record_number']#でここではRecordNumberFormクラスのrecord_numberのchoiceを選択している
    else:#リクエストがないデフォルトの表示件数を10件にする。
        record_number = 10

    record_number_form = RecordNumberForm()  # RecordNumberFormのインスタンス化→paramsに渡す
    record_number_form.initial = {'record_number': str(record_number)}  # 初期値(開いた時に件数として表示されるやつの設定)


#並び替えの部分

    # if 'record_order' in request.session:#？なんでここみたいにrecord_numberのとこはセッションにまだ何もない場合のためのif文を書かなくてもいいのか？
                                        #レコードの変更をしている場合＝セッションにrecord_orderが格納されている
    if 'record_order' in request.session:
        record_order = request.session['record_order']
        if record_order == 'new':
            memos = Memo.objects.filter(user=request.user).order_by('update_datetime').reverse()#新しい順
        else:
            memos = Memo.objects.filter(user=request.user).order_by('update_datetime')
    else:#デフォルトの設定
        record_order = 'old'
        memos = Memo.objects.filter(user=request.user).order_by('update_datetime')  # 古い順

    record_order_form = SetRecordForm() #form.py のクラスをインスタンス化→paramsに渡す
    record_order_form.initial = {'record_order': record_order}



#ページ移行実装部分
    page = Paginator(memos, record_number)


#htmlで使う変数部分
    params = {
        'page': page.get_page(now_page),#指定されたページにあるオブジェクトをとってくる。
        'form': PostForm(),#これが抜けていたためテキストエリアが表示されへんかった
        'record_number_form': record_number_form,
        'record_order_form': record_order_form,
    }
    return render(request, 'index.html', params)#renderメソッドの第三引数に変数(辞書型)を入れることで、templateのhtmlファイルに使う変数を渡せる、辞書に使う変数を全部格納してしまう



def post(request):
    form = PostForm(request.POST, instance=Memo())
    if form.is_valid(): #validateで検証という英単語だから、formの内容が有効かどうかを観察するためのis_valid
        user = get_user_model().objects.get(id=request.user.id)#ユーザーごとの表示のため
        memo = Memo(content=request.POST.get('content'), user=user)#ユーザーごとの表示のため
        memo.save()#ユーザーごとの表示のため
    else:
        print(form.errors)
    return redirect(to='/')


