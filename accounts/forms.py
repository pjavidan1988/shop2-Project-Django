from django import forms
from django.contrib.auth.models import User


class userRegisterForm(forms.Form):
    user_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    password_1 = forms.CharField(max_length=50)
    password_2 = forms.CharField(max_length=50)

    def clean_user_name(self):
        user = self.cleaned_data['user_name']
        if User.objects.filter(username=user).exists():
            raise forms.ValidationError('این نام کاربری قبلا ثبت شده است')
        return user

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('این ایمیل قبلا ثبت شده است')
        return email

    def clean_password_2(self):
        password1 = self.cleaned_data['password_1']
        password2 = self.cleaned_data['password_2']
        if password1 != password2:
            raise forms.ValidationError('رمز های وارد شده با هم یکی نیستند')
        elif len(password1) < 8:
            raise forms.ValidationError('تعداد کاراکترها کمتر از 8 عدد است')
        elif not any(x.isupper() for x in password1):
            raise forms.ValidationError('باید پسورد شما حداقل یک حرف بزرگ داشته باشد')
        return password1


class userLoginForm(forms.Form):
    user = forms.CharField()
    password = forms.CharField()
