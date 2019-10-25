from django import forms
from .models import Memo

#クラス名はPostFormじゃないといけないのか？
#ModelFormとは？
class PostForm(forms.ModelForm):
    class Meta:
        model = Memo
        fields = ['content']
        widgets = {
            'content': forms.Textarea
        }