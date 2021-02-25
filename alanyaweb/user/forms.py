from django import forms
from django.forms.formsets import ManagementForm




class RegisterForm(forms.Form):

    username = forms.CharField(max_length=50,label="kullanıcı adı")
    password = forms.CharField(max_length=20,label="parola",widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=20,label="parolayı doğrula",widget=forms.PasswordInput)

    def clean(self): #django tarafından gelen bi fonksiyon password kontrolü için
        username = self.cleaned_data.get("username")  #dataları almak için kullandık
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and (password != confirm):
            raise forms.ValidationError("parolalar eşleşmiyor")  #sabit hata değişkeni
        
        values = {
            "username":username,
            "password":password
        }

        return values


class LoginForm(forms.Form):
    username = forms.CharField(label="kullanıcı adı")
    password = forms.CharField(label="parola",widget=forms.PasswordInput)

    














