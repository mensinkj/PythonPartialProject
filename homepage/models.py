#
# FILE:     models.py
# AUTHOR:   Stephen W. Liddle
# REVISED BY: GROUP 1-14
# DATE:     21 February 2015
#
# DESCRIPTION:  This is a Django models file that corresponds to our CHF case DCD.
#

from django.db import models
from django.contrib.auth.models import AbstractUser
from polymorphic import PolymorphicModel

class Address(models.Model):
    '''
        A mailing address (in the USA).
    '''
    address1 = models.TextField(max_length=200)
    address2 = models.TextField(max_length=200, null=True, blank=True)
    city = models.TextField(max_length=100)
    state = models.TextField(max_length=20)
    zip_code = models.TextField(max_length=20)

    class Meta:
        ordering = ['state', 'city', 'zip_code', 'address1', 'address2']
        verbose_name_plural = 'addresses'

    def __str__(self):
        return '{} {} {}, {}  {}'.format(self.address1, self.address2, self.city, self.state, self.zip_code)

class LegalEntity(models.Model):
	given_name = models.TextField(max_length=50)
	creation_date = models.DateTimeField(null=True)
	email = models.EmailField(max_length=75, null=True)
	address = models.ForeignKey('Address', null=True, related_name='+')

class Person(LegalEntity):
	family_name = models.TextField(max_length=30)
	
class Organization(LegalEntity):
	organization_type = models.TextField(max_length=30, null=True)

class Photograph(models.Model):
    '''
        A photograph to be used as a user ID photo or a product photo.
    '''
    date_taken = models.DateTimeField(null=True)
    place_taken = models.TextField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    image = models.BinaryField(null=True)

    def __str__(self):
        return self.description

class User(AbstractUser):
    '''
        A user within the CHF system.  Extends the built-in AbstractUser, and so we'll
        need to indicate in our settings.py that this is the designated login user.
    '''
    phone = models.TextField(max_length=40)
    security_question = models.TextField(max_length=200)
    security_answer = models.TextField(max_length=200)
    requires_reset = models.BooleanField(default=False)
    organization_name = models.TextField(max_length=200, null=True, blank=True)
    organization_type = models.TextField(max_length=40, null=True, blank=True)
    date_appointed_agent = models.DateField(null=True)
    relationship = models.TextField(max_length=200, null=True, blank=True)
    emergency_contact = models.TextField(max_length=200, null=True, blank=True)
    emergency_phone = models.TextField(max_length=200, null=True, blank=True)
    emergency_relationship = models.TextField(max_length=200, null=True, blank=True)
    address = models.ForeignKey('Address',null=True, related_name='+')
    id_photo = models.ForeignKey('Photograph',null=True, related_name='+')

    def __str__(self):
        return self.user.username

class PublicEvent(models.Model):
    '''
        A public event such as "The Colonial Heritage Festival".
    '''
    name = models.TextField(max_length=200)
    description = models.TextField(max_length=1000)

class Venue(models.Model):
	'''
        An instance of a venue in which an event can/will be held.
    '''
	name = models.TextField(max_length=200)
	address1 = models.TextField(max_length=200)
	city = models.TextField(max_length=100)
	state = models.TextField(max_length=20)
	zip_code = models.TextField(max_length=20)
	
class Event(models.Model):
    '''
        An instance of a public event, such as "The 2015 Colonial Heritage Festival at Orem".
    '''
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    map_file_name = models.TextField(max_length=200)
    venue_name = models.ForeignKey('Venue',null=True)
    public_event = models.ForeignKey('PublicEvent',null=True)

class HistoricalFigure(models.Model):
    '''
        A historical figure that a participant may portray at an event.
    '''
    name = models.TextField(max_length=200)
    birth_date = models.DateField(null=True)
    birth_place = models.TextField(max_length=200, null=True, blank=True)
    death_date = models.DateField(null=True)
    death_place = models.TextField(max_length=200, null=True, blank=True)
    biographical_note = models.TextField(null=True)
    is_fictional = models.BooleanField(default=False)

class ParticipantRole(models.Model):
    '''
        This class identifies the relationship between a user who is a participant and
        the area(s) in which s/he participates.
    '''
    participant = models.ForeignKey('User',null=True) 
    area = models.ForeignKey('Area',null=True)
    name = models.TextField(max_length=200)
    type = models.TextField(max_length=40)
    historical_figure = models.ForeignKey('HistoricalFigure',null=True)

class Area(models.Model):
    '''
        An area of an event may represent an exhibit, a first aid station, or some other
        distinct element within the event.
    '''
    name = models.TextField(max_length=200)
    description = models.TextField(max_length=1000)
    place_number = models.PositiveIntegerField()
    event = models.ForeignKey('Event',null=True)

class ExpectedSaleItem(models.Model):
    name = models.TextField(max_length=200)
    description = models.TextField(max_length=1000)
    low_price = models.DecimalField(max_digits=10, decimal_places=2)
    high_price = models.DecimalField(max_digits=10, decimal_places=2)

class Transaction(models.Model):
    date = models.DateTimeField()
    phone = models.TextField()
    date_packed = models.DateTimeField()
    date_paid = models.DateTimeField(null=True)
    date_shipped = models.DateTimeField(null=True)
    tracking_number = models.FloatField(null=True)
    ships_to = models.ForeignKey('Address',null=True, related_name='+')
    packed_by = models.ForeignKey('User', null=True,related_name='packedby_set')
    payment_handler = models.ForeignKey('User',null=True, related_name='payment_handler_set')
    shipped_by = models.ForeignKey('User', null=True,related_name='shippedby_set')
    handled_by = models.ForeignKey('User', null=True,related_name='handledby_set')
    customer = models.ForeignKey('User', null=True,related_name='orders')

class LineItem(models.Model):
    '''
        Abstract base class for line items in a transaction.  A line item can be one
        of sale item, fee, rental item, or service item.
    '''
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction = models.ForeignKey('Transaction',null=True)

    class Meta:
        abstract = True

class Category(models.Model):
    '''
        Category within the product catalog.
    '''
    description = models.TextField(max_length=200)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.description

class ProductSpecification(models.Model):
    '''
        The specification of a product that is in our catalog.
    '''
    name = models.TextField(max_length=200, null=True)
    price = models.DecimalField(max_digits=10, null=True, decimal_places=2)
    description = models.TextField(null=True)
    manufacturer = models.TextField(max_length=80, null=True)
    average_cost = models.DecimalField(max_digits=10, null=True, decimal_places=2)
    sku = models.TextField(max_length=20, null=True)
    order_form_name = models.TextField(max_length=200, null=True)
    production_time = models.TextField(max_length=200, null=True)
    category = models.ForeignKey(Category, null=True, related_name='+')
    photo = models.OneToOneField(Photograph, null=True)

    def __str__(self):
        return '{} {}'.format(self.name, self.price)

class StockedProduct(PolymorphicModel):
    '''
        A product in our inventory.  This concrete class represents bulk products
        that only need their quantity and location to be tracked.  There are concrete
        subclasses for serialized and rental products.
    '''
    quantity_on_hand = models.IntegerField()
    shelf_location = models.TextField(max_length=40)
    order_file = models.TextField(null=True)
    product_specification = models.ForeignKey(ProductSpecification,null=True, related_name='+')

    def __str__(self):
        return '{}'.format(self.quantity_on_hand)

class SerializedProduct(StockedProduct):
    '''
        A specific item in our inventory, identified by a serial number.
        Quantity on hand is constrained to be at most one for a
        serialized product.  This is a concrete subclass of StockedProduct,
        and there is a concrete subclass of this class called RentalProduct.
    '''
    serial_number = models.TextField(max_length=100, unique=True, null=True)
    date_acquired = models.DateField(auto_now_add=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.TextField(max_length=40)
    for_sale = models.BooleanField(default=True)
    condition_new = models.BooleanField(default=True)
    note = models.TextField(max_length=250)
    owner1 = models.ForeignKey(LegalEntity, null=True)

    def __str__(self):
        return '{} {}'.format(self.serial_number, self.status)

class WardrobeItem(SerializedProduct):
    '''
        A wardrobe item in our inventory.
    '''
    size = models.TextField(max_length=40)
    size_modifier =models.TextField(max_length=40)
    gender = models.TextField(max_length=40)
    color = models.TextField(max_length=40)
    pattern = models.TextField(max_length=40)
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField()

class RentalProduct(WardrobeItem):
    '''
        A specific item in our inventory that we are willing to rent.
    '''
    times_rented = models.IntegerField()
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    replacement_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return '{} {} {}'.format(self.times_rented, self.price_per_day, self.replacement_price)

class RentalItem(LineItem):
    date_out = models.DateTimeField(auto_now_add=True)
    date_in = models.DateTimeField()
    date_due = models.DateTimeField()
    discount_percent = models.DecimalField(max_digits=3, decimal_places=0)
    rental_product = models.ForeignKey(RentalProduct,null=True, related_name='+')

    def __str__(self):
        return '{} {} {}'.format(self.date_out, self.date_due, self.date_in)

class Fee(LineItem):
    '''
        Abstract base class for the various fee types.  Concrete fee types
        include late and damage fees.  The maximum fee amount should be the purchase
        price of the rental product less the rental fee.
    '''
    waived = models.BooleanField(default=False)
    rental_item = models.ForeignKey(RentalItem, null=True,related_name='+')

    class Meta:
        abstract = True

class LateFee(Fee):
    '''
        A late fee for an item rental.  This is a concrete subclass of Fee.
        For now we use the daily rental price as the per-day late fee.
    '''
    days_late = models.PositiveIntegerField()

    def __str__(self):
        return '{} {} {}'.format(self.amount, self.days_late, self.waived)

class DamageFee(Fee):
    '''
        A damage fee for an item rental.  This is a concrete subclass of Fee.
    '''
    description = models.TextField()

    def __str__(self):
        return '{} {} {}'.format(self.amount, self.description, self.waived)

class SaleItem(LineItem):
    '''
        A sale item for either a bulk or a serialized product.
    '''
    quantity = models.IntegerField()
    product = models.ForeignKey(StockedProduct, null=True,related_name='+')

    def __str__(self):
        return '{} {}'.format(self.amount, self.quantity)


class Rentals(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    quantity = models.IntegerField()
    date_out = models.DateField()
    date_in = models.DateField(null=True)
    date_due = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    damage_fee = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, related_name='user')
    days_late=models.IntegerField()