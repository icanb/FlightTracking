

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin as exportadmin
from webapp.models import Flight, FlightDataResource, House, HouseDataResource, User, UserDataResource


class FlightModelAdmin(exportadmin):
    pass


admin.site.register(Flight, FlightModelAdmin)


class HouseModelAdmin(exportadmin):
    pass


admin.site.register(House, HouseModelAdmin)


admin.site.register(User, UserAdmin)
