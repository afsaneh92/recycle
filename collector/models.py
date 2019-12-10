from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
from django.urls import reverse


class Receiver(models.Model):

    fullname = models.CharField(max_length=40, verbose_name='نام کامل')
    mobile_number = models.CharField(max_length=40, verbose_name='شماره همراه')
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                verbose_name='مدیر',related_name='receivers', default=User.username)

    def get_absolute_url(self):
        return reverse('collector:receiver_detail', args=[str(self.id)])


class MobileUser(models.Model):

    mobile_number = models.CharField(max_length=40, verbose_name='شماره همراه')
    fullname = models.CharField(max_length=40, verbose_name='نام کامل')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='mobile_user')


class RecyclingRequest(models.Model):

    requester = models.ForeignKey('MobileUser', on_delete=models.SET_NULL, null=True,
                                  verbose_name='درخواست دهنده', related_name='user_requests')
    receiver = models.ForeignKey('Receiver', on_delete=models.SET_NULL, null=True,
                                 verbose_name='دریافت کننده', related_name='receiver_requests')
    address = models.TextField(blank=False, verbose_name='آدرس')

    RECYCLE_STATUS = (
        ('ثبت اطلاعات', 'ثبت اطلاعات'),
        ('تعیین پذیرنده', 'تعیین پذیرنده'),
        ('حذف درخواست', 'حذف درخواست'),
    )

    status = models.CharField(max_length=40, choices=RECYCLE_STATUS, blank=True,
                              default='ثبت اطلاعات', verbose_name='وضعیت')

    TRASH_TYPE = (
        ('خشک', 'خشک'),
        ('تر', 'تر'),
        ('کاغذ', 'کاغذ'),
        ('فلز', 'فلز'),
    )
    trash_type = models.CharField(max_length=40, choices=TRASH_TYPE,
                                  default='خشک', verbose_name='نوع زباله')
