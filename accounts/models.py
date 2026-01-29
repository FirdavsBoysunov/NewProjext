from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from utils.models import ModelWithTimeStamp
from .manager import AdminManager, CustomerManager, IndividualManager, MarketManager

class CustomUser(AbstractUser, ModelWithTimeStamp):
    class UserTypeEnum(models.TextChoices):
        ADMIN = 'admin', _('admin')
        CUSTOMER = 'customer', _('customer')
        INDIVIDUAL ='individual', _('individual')
        MARKET ='market', _('market')

    user_type = models.CharField(verbose_name=_("user_type"), max_length=100, choices=UserTypeEnum.choices, default=UserTypeEnum.CUSTOMER, blank=True)
    phone = models.CharField(verbose_name=_('phone_number'), max_length=25, blank=True, null=True)
    address = models.CharField(verbose_name=_('address'), max_length=255, blank=True, null=True)
    license = models.FileField(verbose_name=_('license'), upload_to='License/', blank=True, null=True)
    contact_number = models.CharField(verbose_name=_('contact_number'), max_length=25, blank=True, null=True)
    email_verified = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)


class Customer(CustomUser):

    objects = CustomerManager()

    class Meta:
        proxy = True

class Market(CustomUser):

    objects = MarketManager()

    class Meta:
        proxy = True

class Individual(CustomUser):

    objects = IndividualManager()

    class Meta:
        proxy = True

class Admin(CustomUser):

    objects = AdminManager()

    class Meta:
        proxy = True

