from django.shortcuts import render
from inventory.models import *
from sales.models import *
from django.http import HttpResponseRedirect
from datetime import date
from random import choices, choice, randint
import string
from datetime import date

USED = []
CUSTOMERS = [
    {'company': 'Final Construct', 'contact_name': 'Jim Ballard', 'phone_number': '3178629837', 'street_address': '1902 Industry Rd', 'city': 'Indianapolis', 'state': 'Indiana', 'zipcode': '46235'},
    {'company': 'Core Drilling', 'contact_name': 'Philip Ransom', 'phone_number': '3178936472', 'street_address': '7865 Matthis Ln', 'city': 'Indianapolis', 'state': 'Indiana', 'zipcode': '46857'},
    {'company': 'Hopscotch Brewery', 'contact_name': 'Jake Garlen', 'phone_number': '3172367482', 'street_address': '1039 Spring St', 'city': 'Indianapolis', 'state': 'Indiana', 'zipcode': '46235'},
    {'company': 'Reel Pipe Co', 'contact_name': 'Earl Peckins', 'phone_number': '3172098549', 'street_address': '28374 Eikenberry Rd', 'city': 'Indianapolis', 'state': 'Indiana', 'zipcode': '49485'},
    {'company': 'Chewies', 'contact_name': 'James Morris', 'phone_number': '3172435011', 'street_address': '125 Casey Ave', 'city': 'Indianapolis', 'state': 'Indiana', 'zipcode': '46383'},
    {'company': 'Nobelville Gas', 'contact_name': 'Corey Stein', 'phone_number': '3171096453', 'street_address': '992 Tackson Pl', 'city': 'Indianapolis', 'state': 'Indiana', 'zipcode': '46293'},
    {'company': 'Total Design', 'contact_name': 'Nick Penziani', 'phone_number': '3174630751', 'street_address': '1394 Horbertt Rd', 'city': 'Indianapolis', 'state': 'Indiana', 'zipcode': '46229'},
    {'company': 'Mels Diner', 'contact_name': 'Mack Demorison', 'phone_number': '3171253671', 'street_address': '9385 MLK Blvd', 'city': 'Indianapolis', 'state': 'Indiana', 'zipcode': '46223'},
    {'company': 'Sun King', 'contact_name': 'Carl Johnson', 'phone_number': '3171768519', 'street_address': '837 Hepson Wy', 'city': 'Indianapolis', 'state': 'Indiana', 'zipcode': '46209'},
    {'company': 'Max Measurment', 'contact_name': 'John Hancock', 'phone_number': '3178092548', 'street_address': '7832 Corporeal St', 'city': 'Indianapolis', 'state': 'Indiana', 'zipcode': '46957'},
    {'company': 'The Pizza Place', 'contact_name': 'Titus Phillips', 'phone_number': '31778632456', 'street_address': '235 Washington St', 'city': 'Indianapolis', 'state': 'Indiana', 'zipcode': '46233'},
    {'company': 'Pacers', 'contact_name': 'Pat Jensson', 'phone_number': '3174138050', 'street_address': '210 Tainted Rd', 'city': 'Indianapolis', 'state': 'Indiana', 'zipcode': '46235'},
    {'company': 'Convention Center', 'contact_name': 'Amy Torent', 'phone_number': '3178093188', 'street_address': '504 Autobahn Rd', 'city': 'Indianapolis', 'state': 'Indiana', 'zipcode': '46222'},
    {'company': 'IBM Bank', 'contact_name': 'John Titus', 'phone_number': '3171456724', 'street_address': '2938 Lepjumper St', 'city': 'Indianapolis', 'state': 'Indiana', 'zipcode': '46235'},
    {'company': 'Fixer Uppers', 'contact_name': 'Adam Shoemaker', 'phone_number': '3173546927', 'street_address': '239 Candlerun Rd', 'city': 'Indianapolis', 'state': 'Indiana', 'zipcode': '46154'},
    {'company': 'Two Guys and a Moped', 'contact_name': 'Candice Ferb', 'phone_number': '3178134508', 'street_address': '1902 Oceanline Rd', 'city': 'Indianapolis', 'state': 'Indiana', 'zipcode': '41352'},
    {'company': 'Bobs CO2', 'contact_name': 'Matthew Corpus', 'phone_number': '3172157658', 'street_address': '1293 Blue Ln', 'city': 'Indianapolis', 'state': 'Indiana', 'zipcode': '46235'},
    {'company': 'Tour of Italy', 'contact_name': 'Tiny Tim', 'phone_number': '3178966877', 'street_address': '1098 800 N Rd', 'city': 'Indianapolis', 'state': 'Indiana', 'zipcode': '46234'},
    {'company': 'Mackenzies', 'contact_name': 'Jim Mackenzie', 'phone_number': '3171542389', 'street_address': '928 Carol Rd', 'city': 'Indianapolis', 'state': 'Indiana', 'zipcode': '46230'},
    {'company': 'Steak Eatery', 'contact_name': 'Haley Wilson', 'phone_number': '3171875948', 'street_address': '127 German Church Rd', 'city': 'Indianapolis', 'state': 'Indiana', 'zipcode': '46219'},
]
TODAY = date.today()
SHIP_DATES = ['2017-12-07', '2017-12-07', '2017-12-07', '2017-12-07', '2017-12-08', '2017-12-09', '2017-12-11', '2017-12-14',]
COURIERS = ['EZ', 'DART', 'DAYTON', 'CITYSHIP']

ICE_3 = 'ICE_3'
ICE_16 = 'ICE_16'
ICE_BLOCK = 'ICE_BLOCK'
BAGGED_ICE_16 = 'BAGGED_ICE_16'
BAGGED_ICE_3 = 'BAGGED_ICE_3'
TUB_FILL_CHOICES = (
    ICE_3,
    ICE_16,
    ICE_BLOCK,
    BAGGED_ICE_3,
    BAGGED_ICE_16,
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
BOTTLE_FILL_CHOICES = (
    ACETYLENE,
    ARGON,
    BEER_GAS,
    CARBON_DIOXIDE,
    GUINNESS_GAS,
    HELIUM,
    MIX_C2,
    MIX_C10,
    MIX_C25,
    NITROGEN,
    OXYGEN,
    STARGON,
    SYPHON,
)
BOTTLE_SIZE_CHOICES = (
    'T',
    'K',
    'S',
    'D',
    'Q',
    'R',
    '50',
    '40',
    '20',
    '15',
    '10',
    '5',
    '2.5',
)

def index(request):
    return render(request, 'Final/index.html')


# ==================== TESTING PURPOSES ==================== #
def testing(request):
    return render(request, 'Final/testing.html')


def add_tubs(request):
    for i in range(100):
        while True:
            serial_number = ''.join(choices(string.ascii_uppercase + string.digits, k=10))
            if serial_number in USED:
                continue
            else:
                USED.append(serial_number)
                break
        barcode = "SUT{}".format((Tub.objects.count() + Bottle.objects.count()) + 1)
        a = Tub()
        a.status = 'DE'
        a.fill = choice(Tub.FILL_CHOICES)
        a.barcode = barcode
        a.serial_number = serial_number
        a.emp_init = 'dp'
        a.save()

    return HttpResponseRedirect('/testing/')


def del_tubs(request):
    Tub.objects.all().delete()
    return HttpResponseRedirect('/testing/')


def add_bottles(request):
    for i in range(100):
        while True:
            serial_number = ''.join(choices(string.ascii_uppercase + string.digits, k=10))
            if serial_number in USED:
                continue
            else:
                USED.append(serial_number)
                break
        barcode = "SUT{}".format((Tub.objects.count() + Bottle.objects.count()) + 1)
        a = Bottle()
        a.status = 'DE'
        a.fill = choice(Bottle.FILL_CHOICES)
        a.size = choice(Bottle.SIZE_CHOICES)
        a.barcode = barcode
        a.serial_number = serial_number
        a.emp_init = 'dp'
        a.save()

    return HttpResponseRedirect('/testing/')


def del_bottles(request):
    Bottle.objects.all().delete()
    return HttpResponseRedirect('/testing/')


def add_customers(request):
    for i in range(20):
        a = Customer()
        a.company = CUSTOMERS[i-1]['company']
        a.contact_name = CUSTOMERS[i-1]['contact_name']
        a.phone_number = CUSTOMERS[i-1]['phone_number']
        a.customer_id = (Customer.objects.count() + 1)
        a.street_address = CUSTOMERS[i-1]['street_address']
        a.city = CUSTOMERS[i-1]['city']
        a.state = CUSTOMERS[i-1]['state']
        a.zipcode = CUSTOMERS[i-1]['zipcode']
        a.save()
    return render(request, 'Final/testing.html')


def del_customers(request):
    Customer.objects.all().delete()
    return HttpResponseRedirect('/testing/')


def add_orders(request):
    for i in range(30):
        a = Order()
        a.date_ordered = '2017-12-01'
        a.ship_date = choice(SHIP_DATES)
        a.emp_init = 'DJP'
        a.customer = choice((Customer.objects.all()))
        a.po_number = '.'
        a.branch = '1'
        a.ship_method = 'Courier'
        a.courier = choice(COURIERS)
        a.order_type = 'CHARGE'
        a.status = choice(['SHIPPED', 'QUEUED'])
        a.save()
        hm_tubs = randint(0, 5)
        t = Tub.objects.all().count() - Tub.objects.filter(status='DE').count()
        for j in range(hm_tubs):
            qfill = choice(TUB_FILL_CHOICES)
            a.queuedtub_set.create(
                fill=qfill,
            )
            if a.status == 'SHIPPED':
                tubs = Tub.objects.all().order_by('barcode')
                tub = Tub.objects.get(barcode=tubs[t].barcode)
                t += 1
                tub.fill = qfill
                tub.status = 'CS'
                tub.order = a
                tub.save()

        hm_bottles = randint(0, 5)
        b = Bottle.objects.all().count() - Bottle.objects.filter(status='DE').count()
        for j in range(hm_bottles):
            qfill = choice(BOTTLE_FILL_CHOICES)
            qsize = choice(BOTTLE_SIZE_CHOICES)
            a.queuedbottle_set.create(
                fill=qfill,
                size=qsize,
            )
            if a.status == 'SHIPPED':
                bottles = Bottle.objects.all().order_by('barcode')
                bottle = Bottle.objects.get(barcode=bottles[b].barcode)
                b += 1
                bottle.fill = qfill
                bottle.size = qsize
                bottle.status = 'CS'
                bottle.order = a
                bottle.save()
    return render(request, 'Final/testing.html')


def del_orders(request):
    Order.objects.all().delete()
    return HttpResponseRedirect('/testing/')