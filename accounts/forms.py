from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput
from phone_field import PhoneField

from accounts.models import Profile


class userRegisterForm(forms.Form):
    user_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder':'لطفا نام کاربری خود را وارد کنید'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'لطفا ایمیل خود را وارد کنید'}))
    first_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder':'لطفا نام  خود را وارد کنید'}))
    last_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder':'لطفا نام خانوادگی خود را وارد کنید'}))
    password_1 = forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'placeholder':'لطفا پسورد خود را وارد کنید'}))
    password_2 = forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'placeholder':'تکرار پسورد'}))

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
    user = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'لطفا نام کاربری یا ایمیل خود را وارد کنید'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'لطفا پسورد خود را وارد کنید'}))


class userUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        help_texts = {
            'username': None,
        }
        widgets = {
            'username': TextInput(attrs={'class': 'input', 'placeholder':'نام کاربری'}),
            'email': EmailInput(attrs={'class': 'input', 'placeholder': 'ایمیل'}),
            'first_name': TextInput(attrs={'class': 'input', 'placeholder': 'نام'}),
            'last_name': TextInput(attrs={'class': 'input', 'placeholder': 'نام خانوادگی'}),
        }
        error_messages = {'invalid': 'your custom error message'}

class profileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone', 'address','postal_code', 'city')

        widgets = {'city': TextInput(attrs={'class': 'input', 'placeholder': 'شهر'}),
                   'address': TextInput(attrs={'class': 'input', 'placeholder': 'آدرس'}),
                   'postal_code': TextInput(attrs={'class': 'input', 'placeholder': 'کد پستی'})}
        error_messages = {'invalid': 'your custom error message'}


class phoneForm(forms.Form):
    phone = forms.IntegerField()