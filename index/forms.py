from django import forms


class TitleSearch(forms.Form):
    title = forms.CharField(label='书名', label_suffix='', error_messages={'required': '请输入正确的title'})


class TestForm(forms.Form):
    a = forms.CharField(required=False)
    b = forms.CharField(max_length=20)
    c = forms.IntegerField(max_value=10, min_value=1)


class NameForm(forms.Form):
    your_name = forms.CharField(max_length=12, min_length=4, label='Your name')
