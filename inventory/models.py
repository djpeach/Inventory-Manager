from django.db import models
from django.urls import reverse
from sales.models import *

# Create your models here.
class Tub(models.Model):
    TRUCK = 'TK'
    CUSTOMER = 'CS'
    DOCKED_EMPTY = 'DE'
    DOCKED_FULL = 'DF'
    STATUS_CHOICES = (
        (TRUCK, 'On Truck'),
        (CUSTOMER, 'Customer Site'),
        (DOCKED_FULL, 'Docked Full'),
        (DOCKED_EMPTY, 'Docked Empty'),
    )
    ICE_3 = 'ICE_3'
    ICE_16 = 'ICE_16'
    ICE_BLOCK = 'ICE_BLOCK'
    BAGGED_ICE_16 = 'BAGGED_ICE_16'
    BAGGED_ICE_3 = 'BAGGED_ICE_3'
    FILL_CHOICES = (
        (ICE_3, '3 Mill'),
        (ICE_16, '16 Mill'),
        (ICE_BLOCK, 'Ice Block'),
        (BAGGED_ICE_3, '3 Mill Bagged'),
        (BAGGED_ICE_16, '16 Mill Bagged'),
    )
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=DOCKED_EMPTY)
    fill = models.CharField(max_length=13, choices=FILL_CHOICES, default=ICE_3)
    barcode = models.CharField(max_length=15, unique=True)
    serial_number = models.CharField(max_length=15, unique=True, primary_key=True)
    emp_init = models.CharField(max_length=3)
    order = models.ForeignKey(Order, null=True, blank=False, on_delete=models.CASCADE)

    # This controls where the user gets taken when a new object is created
    @staticmethod
    def get_absolute_url():
        return reverse('warehouse:tubs')

    def __str__(self):
        return "{}-{}-{}, {} by {}".format(self.fill, self.barcode, self.serial_number, self.status, self.emp_init)


class Bottle(models.Model):
    TRUCK = 'TK'
    CUSTOMER = 'CS'
    DOCKED_EMPTY = 'DE'
    DOCKED_FULL = 'DF'
    RETEST = 'RT'
    STATUS_CHOICES = (
        (TRUCK, 'On Truck'),
        (CUSTOMER, 'Customer Site'),
        (DOCKED_FULL, 'Docked Full'),
        (DOCKED_EMPTY, 'Docked Empty'),
        (RETEST, 'Retest'),
    )
    ACETYLENE = 'AC'
    ARGON = 'AR'
    BEER_GAS = 'BG'
    CARBON_DIOXIDE = 'CD'
    GUINNESS_GAS = 'GS'
    HELIUM = 'HE'
    MIX_C2 = 'C2'
    MIX_C10 = 'C10'
    MIX_C25 = 'C25'
    NITROGEN = 'NI'
    OXYGEN = 'OX'
    STARGON = 'ST'
    SYPHON = 'SY'
    FILL_CHOICES = (
        (ACETYLENE, 'Acetylene'),
        (ARGON, 'Argon'),
        (BEER_GAS, 'Beer Gas'),
        (CARBON_DIOXIDE, 'Carbon Dioxide'),
        (GUINNESS_GAS, 'Guinness Gas'),
        (HELIUM, 'Helium'),
        (MIX_C2, 'Mix C2'),
        (MIX_C10, 'Mix C10'),
        (MIX_C25, 'Mix C25'),
        (NITROGEN, 'Nitrogen'),
        (OXYGEN, 'Oxygen'),
        (STARGON, 'Stargon'),
        (SYPHON, 'Syphon'),
    )
    SIZE_CHOICES = (
        ('T', 'T'),
        ('K', 'K'),
        ('S', 'S'),
        ('D', 'D'),
        ('Q', 'Q'),
        ('R', 'R'),
        ('50', '50'),
        ('40', '40'),
        ('20', '20'),
        ('15', '15'),
        ('10', '10'),
        ('5', '5'),
        ('2.5', '2.5'),
    )
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=DOCKED_FULL)
    fill = models.CharField(max_length=3, choices=FILL_CHOICES)
    size = models.CharField(max_length=3, choices=SIZE_CHOICES, default='T')
    barcode = models.CharField(max_length=15, unique=True)
    serial_number = models.CharField(max_length=15, unique=True, primary_key=True)
    emp_init = models.CharField(max_length=3)
    order = models.ForeignKey(Order, null=True, blank=False, on_delete=models.CASCADE)

    # This controls where the user gets taken when a new object is created
    @staticmethod
    def get_absolute_url():
        return reverse('warehouse:bottles')

    def __str__(self):
        return "{} {}-{}-{}-{} by {}".format(self.fill, self.size, self.status, self.barcode, self.serial_number, self.emp_init)