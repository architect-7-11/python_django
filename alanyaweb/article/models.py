from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.fields.json import DataContains
from django.urls import reverse
# Create your models here.

class category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("index")
    


class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="yazar")
    title = models.CharField(max_length=50,verbose_name="başlık")

    kategori = models.CharField(max_length=255,default="coding")

    content = RichTextField()
    created_date = models.DateField(auto_now_add=True,verbose_name="oluşturulma tarihi")
    article_image = models.FileField(blank=True,null=True,verbose_name="makaleye fotoğraf ekleyin")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']
    
class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="Makale",related_name="comments")
    comment_author = models.CharField(max_length=50,verbose_name="İsim")
    comment_content = models.CharField(max_length=200,verbose_name="Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_content


    class Meta:
        ordering = ['-comment_date']















