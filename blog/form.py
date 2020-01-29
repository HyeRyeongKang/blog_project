from django import forms
from .models import Blog

#class BlogPost(forms.ModelForm):
 #   class Meta:
  #      model=Blog  # 어떤 모델 기반
   #     fields=['title', 'body']    # 입력받을 공간

class BlogPost(forms.Form):
    email=forms.EmailField()
    files=forms.FileField()
    url=forms.URLField()
    words=forms.CharField(max_length=200)
    max_number=forms.ChoiceField(choices=[('1', 'one'), ('2', 'two'), ('3', 'three')])
