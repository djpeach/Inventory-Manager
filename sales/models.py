from django.db import models
from django.shortcuts import reverse


# Create your models here.


class Customer(models.Model):
    company = models.CharField(max_length=100, unique=True)
    contact_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10, unique=True)
    customer_id = models.AutoField(primary_key=True)
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=5)

    @staticmethod
    def get_absolute_url():
        return reverse('sales:customers')

    def __str__(self):
        return ' '.join([self.company, str(self.customer_id)])


class Order(models.Model):
    STATUS_CHOICES = (
        ('QUEUED', 'Queued'),
        ('SHIPPED', 'Shipped'),
    )
    order_number = models.AutoField(primary_key=True, unique=True)
    date_ordered = models.DateField()
    ship_date = models.DateField()
    emp_init = models.CharField(max_length=3)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    po_number = models.CharField(max_length=50, null=True, blank=True)
    branch = models.IntegerField(default=1)
    ship_method = models.CharField(max_length=50, null=True, blank=True)
    courier = models.CharField(max_length=50, null=True, blank=True)
    order_type = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True, choices=STATUS_CHOICES, default='QUEUED')

    def __str__(self):
        return "{} - {} - {} id: {}".format(self.customer, self.ship_date, self.order_number, self.order_number)


class QueuedTub(models.Model):
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
    fill = models.CharField(max_length=13, choices=FILL_CHOICES)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return "Dry Ice Tub: {}".format(self.fill)

class QueuedBottle(models.Model):
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
    fill = models.CharField(max_length=13, choices=FILL_CHOICES)
    size = models.CharField(max_length=3, choices=SIZE_CHOICES)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return "Gas Bottle: {} {}".format(self.fill, self.size)



