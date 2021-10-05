from django import forms


class TitleSearch(forms.Form):
    title = forms.CharField(label='书名', widget=forms.Textarea)
