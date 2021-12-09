from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# from phone_field import PhoneField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name = 'نام')
    phone = models.IntegerField(blank=True, null=True, max_length=11, verbose_name = 'تلفن')
    address = models.CharField(blank=True, null=True, max_length=300, verbose_name = 'آدرس')
    postal_code = models.CharField(blank=True, null=True, max_length=10, verbose_name = 'کد پستی')
    city = models.CharField(blank=True, null=True, max_length=30, verbose_name = 'شهر')

    def __str__(self):
        return self.user.username


def save_profile_user(sender, **kwargs):
    if kwargs['created']:
        profile_user = Profile(user=kwargs['instance'])
        profile_user.save()


post_save.connect(save_profile_user, sender=User)
