from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import UserProfileManager

class User(AbstractUser):
    
    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)

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
        max_length=30,
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


class CargoStatus(models.Model):
    
    name = models.CharField(
        max_length=30,
        verbose_name=_('Name')
    )

    code = models.CharField(
        max_length=30,
        unique=True,
        verbose_name=_('Code')
    )

    class Meta:
        verbose_name = _('Cargo Status')
        verbose_name_plural = _('Cargo Statuses')
    
    def __str__(self):
        return self.name


class Cargo(models.Model):

    route = models.TextField(
        verbose_name=_('Route')
    )

    state = models.ForeignKey(
        State,
        on_delete=models.RESTRICT,
        verbose_name=_('State')
    )

    numberOfDeliveries = models.IntegerField(
        verbose_name=_('Number of deliveries')
    )

    weightInKg = models.IntegerField(
        verbose_name=_('Weight in Kg')
    )

    payment = models.FloatField(
        verbose_name=_('Payment')
    )

    advancePayment = models.FloatField(
        verbose_name=_('Advance payment')
    )

    status = models.ForeignKey(
        CargoStatus,
        on_delete=models.RESTRICT,
        verbose_name=_('Status')
    )

    driverName = models.CharField(
        max_length=60,
        verbose_name=_('Driver name'),
        blank=True
    )

    driverPhone = models.CharField(
        max_length=15,
        verbose_name=_('Driver phone'),
        blank=True
    )

    note = models.TextField(
        verbose_name=_('Note'),
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created At')
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Updated At')
    )
    
    class Meta:
        verbose_name = _('Cargo')
        verbose_name_plural = _('Cargoes')
    
    def __str__(self):
        return self.route

class CargoStatusChange(models.Model):
    
    cargo = models.ForeignKey(
        Cargo,
        on_delete=models.CASCADE,
        verbose_name=_('Cargo')
    )

    old_status = models.ForeignKey(
        CargoStatus,
        on_delete=models.RESTRICT,
        verbose_name=_('Old status'),
        related_name='status_changes_old'
    )

    new_status = models.ForeignKey(
        CargoStatus,
        on_delete=models.RESTRICT,
        verbose_name=_('New status'),
        related_name='status_changes_new'
    )

    timestamp = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Timestamp')
    )

    class Meta:
        verbose_name = _('Cargo Status Change')
        verbose_name_plural = _('Cargo Status Changes')

    def __str__(self):
        return f'[{self.timestamp}] {self.old_status.name} -> {self.new_status.name}'