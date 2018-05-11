#!/usr/bin/env python3

import random
import os
import datetime
import sys

# initialize the django environment
# assumes ./proj/settings.py is your settings file, relative to current dir
os.environ['DJANGO_SETTINGS_MODULE'] = 'test_dmp.settings'
import homepage.models as hmod
import django
django.setup()

from django.contrib.auth.models import Group, Permission, ContentType
from django.db import connection
import subprocess

#Drop database schema and recreate ########################################
cursor = connection.cursor()
cursor.execute("DROP SCHEMA PUBLIC CASCADE")
cursor.execute("CREATE SCHEMA PUBLIC")
subprocess.call([sys.executable, "manage.py", "migrate"])

#Create groups and permissions

Permission.objects.all().delete()
Group.objects.all().delete()

permission3 = Permission()
permission3.codename = 'check_user'
permission3.content_type = ContentType.objects.get(id=8)
permission3.name = 'check_user'
permission3.save()

group3 = Group()
group3.name = "user"
group3.save()
group3.permissions.add(permission3)

permission2 = Permission()
permission2.codename = 'check_manager'
permission2.content_type = ContentType.objects.get(id=8)
permission2.name = 'check_manager'
permission2.save()

group2 = Group()
group2.name = "manager"
group2.save()
group2.permissions.add(permission2)
group2.permissions.add(permission3)

permission1 = Permission()
permission1.codename = 'check_admin'
permission1.content_type = ContentType.objects.get(id=8)
permission1.name = 'check_admin'
permission1.save()

group1 = Group()
group1.name = "Admin"
group1.save()
group1.permissions.add(permission1)
group1.permissions.add(permission2)
group1.permissions.add(permission3)
# create data

hmod.User.objects.all().delete()
u = hmod.User()
u.first_name = "Joshua"
u.last_name = "Mensink"
u.email = "Josh@gmail.com"
u.set_password('password')
u.username = "admin"
u.is_superuser = True
u.save()
group1.user_set.add(u)

u = hmod.User()
u.first_name = "Brooke"
u.last_name = "Mensink"
u.email = "Brooke@gmail.com"
u.set_password('password')
u.username = "manager"
u.save()
group2.user_set.add(u)

u = hmod.User()
u.first_name = "Tommy"
u.last_name = "Mensink"
u.email = "Tommy@gmail.com"
u.set_password('password')
u.username = "user"
u.save()
group3.user_set.add(u)

a = hmod.Address()
a.address1 = "123 fake street"
a.address2 = "colonial heritage"
a.city = "Provo"
a.state = "Utah"
a.zip_code = "84604"
a.save()

a = hmod.Address()
a.address1 = "456 fake street"
a.address2 = "colonial heritage 2"
a.city = "Orem"
a.state = "Utah"
a.zip_code = "84604"
a.save()

l = hmod.LegalEntity()
l.given_name = "awesomeness"
l.email = "legalentity@gmail.com"

l = hmod.LegalEntity()
l.given_name = "josh"
l.email = "josh@gmail.com"

p = hmod.ProductSpecification()
p.name = "Colonial Breeches"
p.price = 10.99
p.description = "Nice Red Colonial Breeches"
p.save()

p = hmod.ProductSpecification()
p.name = "Colonial Mug"
p.price = 5.99
p.description = "Nice Colonial Mug"
p.save()

p = hmod.ProductSpecification()
p.name = "American Flag"
p.price = 10.99
p.description = "The Biggest american flag ever"
p.save()

p = hmod.ProductSpecification()
p.name = "Eagles"
p.price = 999.10
p.description = "What's more american than buying an Eagle"
p.save()

p = hmod.ProductSpecification()
p.name = "Bread"
p.price = 7.99
p.description = "delicious homemade bread"
p.save()

p = hmod.ProductSpecification()
p.name = "Pic with Gove"
p.price = 1.99
p.description = "Get a Picture with Gove Allen"
p.save()

p = hmod.ProductSpecification()
p.name = "fake item1"
p.price = 15.67
p.description = "test item description"
p.save()

a = hmod.Area()
a.name = "area 1"
a.description = "This is the 1st area"
a.place_number = 1
a.save()

a = hmod.Area()
a.name = "area 2"
a.description = "This is the 2nd area"
a.place_number = 2
a.save()

a = hmod.Area()
a.name = "area 3"
a.description = "This is the 3rd area"
a.place_number = 3
a.save()

v = hmod.Venue()
v.name = "Venue 1"
v.address1 = "123 holy moly"
v.city = "Vatican"
v.state = "Italy"
v.zip_code ="666"
v.save()

v = hmod.Venue()
v.name = "Venue 2"
v.address1 = "123 holy moly"
v.city = "Vatican"
v.state = "Italy"
v.zip_code ="666"
v.save()

v = hmod.Venue()
v.name = "Venue 3"
v.address1 = "123 holy moly"
v.city = "Vatican"
v.state = "Italy"
v.zip_code ="666"
v.save()

p = hmod.Person()
p.family_name = "Family Name"
p.save()

o = hmod.Organization()
o.organization_type = "business"
o.save()

p =  hmod.Photograph()
p.place_taken = "Provo"
p.save()

p = hmod.PublicEvent()
p.name = "awesomeness"
p.description = "the place of awesomeness"
p.save()

e = hmod.Event()
e.map_file_name = "this is the map file name"
e.save()

h = hmod.HistoricalFigure()
h.name ="washingtion"
h.save()

p = hmod.ParticipantRole()
p.name = "larry"
p.type = "free"
p.save()

e = hmod.ExpectedSaleItem()
e.name = "sale item"
e.description = "this is the description"
e.low_price = 1.99
e.high_price = 2.99
e.save()

t = hmod.Transaction()
t.date = "2012-01-01"
t.phone = "9872328"
t.date_packed = "2012-01-01"
t.save()

c = hmod.Category()
c.description = "random stuff"
c.save()

s = hmod.StockedProduct()
s.quantity_on_hand = 20
s.shelf_location = "in the back"
s.save()

s = hmod.SerializedProduct()
s.quantity_on_hand = 1
s.serial_number = "sdlkfjslfkd"
s.cost = 342.23
s.status = "new"
s.note = "new"
s.save()

w = hmod.WardrobeItem()
w.quantity_on_hand = 1
w.size = "large"
w.size_modifier = "extra"
w.gender = "male"
w.color = "true blue"
w.pattern = "solid"
w.start_year  = 2012
w.end_year = 2015
w.cost = 123.23
w.save()

r = hmod.RentalProduct()
r.quantity_on_hand = 1
r.times_rented = 12
r.price_per_day = 1.99
r.replacement_price = 500.22
r.cost = 123.23
r.start_year = 2012
r.end_year = 2015
r.save()

r = hmod.RentalItem()
r.date_in = "2012-01-01"
r.date_due = "2012-01-01"
r.discount_percent = .4
r.amount = 123.23
r.save()

l = hmod.LateFee()
l.days_late =  14
l.amount = 432.23
l.save()

d = hmod.DamageFee()
d. description = "completely destroyed"
d.amount = 1232.32
d.save()

s = hmod.SaleItem()
s.quantity = 10
s.amount = 33.33
s.save()

r = hmod.Rentals()
r.name = 'American Flag'
r.quantity = 1
r.description='Your a Grand Ole Flag'
r.date_out = '2015-3-1'
r.date_due = '2015-3-1'
r.price_per_day = 5.00
r.price = 30.00
r.days_late = 35
r.user = hmod.User.objects.get(id=1)
r.damage_fee = 6.00
r.save()

r = hmod.Rentals()
r.name = 'Mayflower Replica'
r.quantity = 1
r.description = 'A giant replica of the mayflower'
r.date_out = '2014-1-20'
r.date_due = '2015-1-20'
r.price_per_day = 20000.00
r.price = 3000000.00
r.days_late = 66
r.user = hmod.User.objects.get(id=1)
r.damage_fee = 6.00
r.save()

r = hmod.Rentals()
r.name = 'Colonial Mug'
r.description = 'mugs for you july 4th party'
r.quantity = 1
r.date_out = '2014-12-1'
r.date_due = '2014-12-1'
r.price_per_day = 1.99
r.price = 10.00
r.days_late = 137
r.user = hmod.User.objects.get(id=1)
r.damage_fee = 6.00
r.save()