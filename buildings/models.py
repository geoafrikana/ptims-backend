from django.contrib.gis.db import models
from django.db.models import F

class BuildingManager(models.Manager):

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).annotate(
            amount_owed=F('tax_paid') - F('tax_due')
        )

# Create your models here.
class Building(models.Model):
    ptin = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    owner = models.CharField(max_length=50, null=True, blank=True)
    category = models.CharField(max_length=50, null=True, blank=True)
    building_type = models.CharField(max_length=50, null=True, blank=True)
    plot_area = models.CharField(max_length=50, null=True, blank=True)
    no_floor = models.CharField(max_length=50, null=True, blank=True)
    no_rooms = models.CharField(max_length=50, null=True, blank=True)
    street = models.CharField(max_length=100, null=True, blank=True)
    house_no = models.CharField(max_length=100, null=True, blank=True)
    year_no = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    condition = models.CharField(max_length=50, null=True, blank=True)
    water_source = models.CharField(max_length=50, null=True, blank=True)
    has_electricity = models.CharField(max_length=50, null=True, blank=True)
    owner_photo = models.ImageField(null=True, blank=True)
    building_photo1 = models.ImageField(null=True, blank=True)
    building_photo2 = models.ImageField(null=True, blank=True)
    building_photo3 = models.ImageField(null=True, blank=True)
    building_photo4 = models.ImageField(null=True, blank=True)
    building_photo5 = models.ImageField(null=True, blank=True)
    tax_due = models.DecimalField(decimal_places=3, max_digits=50, null=True, blank=True )
    tax_paid = models.DecimalField(max_digits=50, decimal_places=3, null=True, blank=True)
    city_name = models.CharField(max_length=50, null=True, blank=True)
    taxable = models.CharField(max_length=50, null=True, blank=True)
    Street_Na = models.CharField(max_length=50, null=True, blank=True)
    number_buildings = models.CharField(max_length=50, null=True, blank=True)
    construction_material = models.CharField(max_length=50, null=True, blank=True)
    number_buildings = models.CharField(max_length=50, null=True, blank=True)
    Buildi_Fin = models.CharField(max_length=50, null=True, blank=True)
    plot_size = models.CharField(max_length=50, null=True, blank=True)

    poly = models.MultiPolygonField()


    objects = BuildingManager()
    
    def __str__(self):
        return self.owner


    