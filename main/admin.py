from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import experiments
#from .models import views

admin.site.register(experiments)
#admin.site.register(ImportExportActionModelAdmin)

#@admin.register(views)
#class viewAdmin(ImportExportActionModelAdmin):
  #  pass
