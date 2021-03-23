from django.contrib import admin
from .models import Country, Province, Area, City

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    search_fields = ('chn_name', 'eng_name',)


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    search_fields = ('chn_name', 'eng_name', )


class CityAdmin(admin.ModelAdmin):
    list_display = ('cityid', 'countryid', 'areaid', 'provinceid', 'chn_name', 'eng_name')
    autocomplete_fields = ['provinceid', 'countryid',]


admin.site.register(Area)
admin.site.register(City, CityAdmin)