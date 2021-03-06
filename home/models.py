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
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )
    name = models.CharField(blank=True, max_length=20)
    email = models.CharField(blank=True, max_length=50)
    subject = models.CharField(blank=True, max_length=50)
    message = models.TextField(blank=True, max_length=255)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=20)
    note = models.CharField(blank=True, max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': TextInput(attrs={'class': 'input-name-checkout form-control', 'placeholder': 'Name & Surname'}),
            'subject': TextInput(attrs={'class': 'input-name-checkout form-control', 'placeholder': 'Subject'}),
            'email': TextInput(attrs={'class': 'input-name-checkout form-control', 'placeholder': 'Email Address'}),
            'message': Textarea(
                attrs={'class': 'input-name-checkout form-control', 'placeholder': 'Your Message', 'rows': '5'}),
        }
