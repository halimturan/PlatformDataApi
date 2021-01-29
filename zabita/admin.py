from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from zabita.models import PazarYerleri
from import_export.admin import ImportExportModelAdmin


class PazarYerleriAdmin(OSMGeoAdmin, ImportExportModelAdmin):
    list_display = ('ilce', 'count', 'point')


admin.site.register(PazarYerleri, PazarYerleriAdmin)

