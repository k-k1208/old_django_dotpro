from django import forms
from .models import Memo

#？クラス名はPostFormじゃないといけないのか
#ModelForm→　Model=　"DB　⇄　Django"、　Form = "Django ⇄　画面"　　ModelForm = "DB ⇄　画面"　
#モデルフォームはモデルに紐ずいたフォームを作ってくれる。例えば↓
#メモ登録はDBと結びつくフォーム→ModelForm　表示件数(RecordNumberForm)はDBと結びつかない→Form
#モデルはデータベース、フォームはHTMLのフォーム

CHOICE_FIELD_RECODE_NUMBERS = (
    ('10', '10件'),
    ('15', '15件'),
    ('30', '30件'),
)

class RecordNumberForm(forms.Form):
    record_number = forms.ChoiceField(
        widget=forms.Select(attrs={'onchange': 'submit(this.form)'}),#ここがわかっていない。onchangeイベントはユーザーの入力に合わせて動的に表示内容を変えられる。
                                                                     #その際のイベント内容が、submit(this.form)ってこと javascriptの範囲である
                                                                     #this.formっていうのはこのフォーム(RecordNumberFormクラスで作られたインスタンスのことだと思われる。

        choices=CHOICE_FIELD_RECODE_NUMBERS
    )

class PostForm(forms.ModelForm):#メタとは「〇〇な〇〇」を「メタ〇〇」という。
                                # クラスのクラスだからメタクラスModelFormクラスを定義するクラスだからPostFormはメタクラス。

    class Meta: #class　Metaを定義すると、例えば親のクラスのメソッドを読み込む際にsuper().親クラスメソッドとか書かなくて良い。
                #親クラスを全く気にせずにかけるようになるおまじない的なもの。メタクラスとは全く関係なし。

        model = Memo
        fields = ['content']
        widgets = {
            'content': forms.Textarea
        }