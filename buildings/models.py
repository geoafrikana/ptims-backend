from django.contrib.gis.db import models

# Create your models here.

class Title(models.Model):
    CONTRACT = 'ctr'
    DEED = 'dee'
    C_OF_O = 'coo'

    TITLE_CHOICES = [
        (CONTRACT, 'Contract'),
        (DEED, 'Deed'),
        (C_OF_O, 'C of O')
    ]
    title = models.CharField(choices=TITLE_CHOICES, max_length=3)

    def __str__(self) -> str:
        return self.title

class Building(models.Model):
    PTIN = models.CharField(max_length=15, null=False, primary_key=True)
    email = models.EmailField()
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)

    RESIDENTIAL ='res'
    COMMERCIAL ='com'
    RELIGIOUS ='rel'
    INDUSTRIAL ='ind'
    INSTITUTIONAL_EDUCATIONAL ='edu'
    LAND = 'lnd'
    BUILDING_USE_CATEGORY = [
        (RESIDENTIAL, 'Residential'),
        (COMMERCIAL, 'Commercial'),
        (RELIGIOUS, 'Residential'),
        (INDUSTRIAL, 'Industrial'),
        (INSTITUTIONAL_EDUCATIONAL, 'Institutional/Educational'),
        (LAND, 'Land'),
    ]
    building_use = models.CharField(
        max_length=3,
        choices=BUILDING_USE_CATEGORY,default=RESIDENTIAL)

    DUPLEX = 'DPX'
    ROOMING_SYSTEM = 'ffy'
    BUNGALOW = 'bgw'
    MULTIPLE_FAMILY_RESIDENCY = 'mfr'

    BUILDING_TYPE_CATEGORY = [
        (DUPLEX, 'Duplex (Storey Building)'),
        (ROOMING_SYSTEM, 'Face me/Face you (Rooming System)'),
        (BUNGALOW, 'Bungalow'),
        (MULTIPLE_FAMILY_RESIDENCY, 'Multiple Family Residency'),
    ]
    building_use = models.CharField(
        max_length=3,
        choices=BUILDING_TYPE_CATEGORY,default=BUNGALOW)

    plot_length = models.IntegerField()
    plot_width = models.IntegerField()
    plot_area = models.IntegerField()
    number_of_floor = models.IntegerField()
    number_of_rooms = models.IntegerField()
    street = models.CharField(max_length=100)
    house_number = models.IntegerField()
    year_of_construction = models.IntegerField()
    
    title = models.ManyToManyField(Title)

    GOOD = 'good'
    REQUIRES_RENOVATION = 'reqr'

    CONDITION_CHOICES = [
        (GOOD, 'Good'),
        (REQUIRES_RENOVATION, 'Requires Renovation'),
    ]
    condition = models.CharField(choices=CONDITION_CHOICES,
     max_length=4)

    PERSONAL_BOREHOLE = 'peb'
    PUBLIC_BOREHOLE = 'pub'
    PUBLIC_TAP = 'put'
    WELL = 'wel'

    WATER_SOURCE_CHOICES = [
        (PERSONAL_BOREHOLE, 'Personal Borehole'),
        (PUBLIC_BOREHOLE, 'Public Borehole'),
        (PUBLIC_TAP, 'Public Tap'),
        (WELL, 'Well'),
    ]

    water_source = models.CharField(choices=WATER_SOURCE_CHOICES,
     max_length=3)
    
    has_electricity = models.BooleanField(default=True)
    owner_photo = models.ImageField(null=True, blank=True)
    building_photo1 = models.ImageField(null=True, blank=True)
    building_photo2 = models.ImageField(null=True, blank=True)
    building_photo3 = models.ImageField(null=True, blank=True)
    building_photo4 = models.ImageField(null=True, blank=True)
    building_photo5 = models.ImageField(null=True, blank=True)
    tax_due = models.DecimalField(max_digits=10, decimal_places=2 )
    tax_paid = models.DecimalField(max_digits=10, decimal_places=2 )

    @property
    def tax_status(self):
        if self.paid == float(0):
            return 'owing'
        elif self.tax_paid == self.tax_due:
            return 'paid'
        elif self.tax_paid < self.tax_due:
            return 'partially paid'  

    poly = models.PolygonField()



    