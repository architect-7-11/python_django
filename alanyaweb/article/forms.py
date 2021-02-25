from django import forms
from django.forms import widgets
from .models import Article,category


# choices = [("çeşitleri","çeşitleri"),("ekim zamanı ve aşılama","ekim zamanı ve aşılama"),("gıda takviyesi","gıda takviyesi"),("güncel bilgiler","güncel bilgiler")]


cats = category.objects.all().values_list("name","name")


our_lists = []
for item in cats:
    our_lists.append(item)



class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title","content","kategori","article_image"]

        widgets = {
            "kategori" : forms.Select(choices=our_lists , attrs={"class":"form-control"})
        }
        




