from django.contrib.gis.utils import LayerMapping
from .models import Building

cleaned_geojson = r"C:\Users\USER\Downloads\mygeodata\cleaned_dozie-polygon.shp"

building_mapping= {
    'ptin':'ptin',
    'email':'email',
    'owner':'owner',
    'category':'category',
    'building_type':'building_t',
    'plot_area':'plot_area',
    'no_floor':'no_floor',
    'no_rooms':'no_rooms',
    'street':'street',
    'house_no':'house_no', 
    'year_no':'year_no',
    'title':'title', 
    'condition':'condition',
    'water_source':'water_sour',
    'has_electricity':'has_electr',
    'tax_due':'tax_due',
    'tax_paid':'tax_paid',
    'city_name':'city_name',
    'taxable':'taxable',
    'Street_Na':'Street_Na',
    'number_buildings':'number_bui',
    'construction_material':'constructi',
    'Buildi_Fin':'Buildi_Fin',
    'plot_size':'plot_size',
    'poly' : 'MULTIPOLYGON',
    }



def run(verbose=True):
    lm = LayerMapping(Building, cleaned_geojson, building_mapping, transform=False)
    lm.save(verbose=verbose)