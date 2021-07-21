from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
from django.forms import TextInput, Textarea, ModelForm


class Setting(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = RichTextUploadingField(blank=True)
    company = models.CharField(max_length=50)
    address = RichTextUploadingField(blank=True)
    phone = models.CharField(blank=True, max_length=15)
    fax = models.CharField(blank=True, max_length=15)
    email = models.CharField(blank=True, max_length=50)
    smtp_server = models.CharField(blank=True, max_length=50)
    smtp_email = models.CharField(blank=True, max_length=50)
    smtp_password = models.CharField(blank=True, max_length=10)
    smtp_port = models.CharField(blank=True, max_length=5)
    icon = models.ImageField(blank=True, upload_to='images/')
    logo = models.ImageField(blank=True, upload_to='images/')
    facebook = models.CharField(blank=True, max_length=50)
    instagram = models.CharField(blank=True, max_length=50)
    twitter = models.CharField(blank=True, max_length=50)
    youtube = models.CharField(blank=True, max_length=50)
    whatsapp = models.CharField(blank=True, max_length=50)
    telegram = models.CharField(blank=True, max_length=50)
    shopping_features_img_1 = models.FileField(blank=True, upload_to='images/')
    shopping_features_title_1 = models.CharField(max_length=150)
    shopping_features_description_1 = models.CharField(max_length=150)
    shopping_features_img_2 = models.FileField(blank=True, upload_to='images/')
    shopping_features_title_2 = models.CharField(max_length=150)
    shopping_features_description_2 = models.CharField(max_length=150)
    shopping_features_img_3 = models.FileField(blank=True, upload_to='images/')
    shopping_features_title_3 = models.CharField(max_length=150)
    shopping_features_description_3 = models.CharField(max_length=150)
    shopping_features_img_4 = models.FileField(blank=True, upload_to='images/')
    shopping_features_title_4 = models.CharField(max_length=150)
    shopping_features_description_4 = models.CharField(max_length=150)
    shopping_features_img_5 = models.FileField(blank=True, upload_to='images/')
    shopping_features_title_5 = models.CharField(max_length=150)
    shopping_features_description_5 = models.CharField(max_length=150)
    aboutus = RichTextUploadingField(blank=True)
    contact = RichTextUploadingField(blank=True)
    references = RichTextUploadingField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class brandImages(models.Model):
    setting = models.ForeignKey(Setting, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    STATUS = (
        ('جدید', 'جدید'),
        ('خوانده شده', 'خوانده شده'),
        ('بستن', 'بستن'),
    )
    name = models.CharField(blank=True, max_length=255, verbose_name='نام')
    email = models.CharField(blank=True, max_length=255, verbose_name='ایمیل')
    phone = models.CharField(blank=True, max_length=11, verbose_name='شماره تلفن')
    subject = models.CharField(blank=True, max_length=255, verbose_name='موضوع')
    message = models.TextField(blank=True, max_length=255, verbose_name='پیام')
    status = models.CharField(max_length=10, choices=STATUS, default='جدید', verbose_name='وضعیت')
    ip = models.CharField(blank=True, max_length=20, verbose_name='ای پی')
    note = models.CharField(blank=True, max_length=255, verbose_name='یادداشت')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, verbose_name='به روز شده در')

    def __str__(self):
        return self.name


class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'phone', 'message']
        widgets = {
            'name': TextInput(attrs={'class': 'input-name-checkout form-control', 'placeholder': 'نام شما'}),
            'subject': TextInput(attrs={'class': 'input-name-checkout form-control', 'placeholder': 'موضوع'}),
            'phone': TextInput(attrs={'class': 'input-name-checkout form-control', 'placeholder': 'شماره تلفن'}),
            'email': TextInput(attrs={'class': 'input-name-checkout form-control', 'placeholder': 'ایمیل شما'}),
            'message': Textarea(attrs={'class': 'input-name-checkout form-control', 'placeholder': 'پیام خود را بنویسید', 'rows': '4'}),
        }
