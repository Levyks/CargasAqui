from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import UserProfileManager

class User(AbstractUser):
    
    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    can_change_password = models.BooleanField(default=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

class State(models.Model):

    code = models.CharField(
        max_length=7,
        verbose_name=_('Code')
    )
    name = models.CharField(
        max_length=255,
        verbose_name=_('Name')
    )
    abbreviation = models.CharField(
        max_length=2,
        verbose_name=_('Abbreviation')
    )

    class Meta:
        verbose_name = _('State')
        verbose_name_plural = _('States')

    def __str__(self):
        return self.name


class City(models.Model):

    code = models.CharField(
        max_length=15,
        verbose_name=_('Code')
    )
    name = models.CharField(
        max_length=255,
        verbose_name=_('Name')
    )
    state = models.ForeignKey(
        State,
        on_delete=models.CASCADE,
        related_name='cities',
        verbose_name=_('State')
    )

    class Meta:
        verbose_name = _('City')
        verbose_name_plural = _('Cities')

    def __str__(self):
        return self.name + ', ' + self.state.abbreviation