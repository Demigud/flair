from django.contrib import admin
from .models import Health

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phonenumber', 'temperature', 'date_joined', 'id')
    #readonly_fields = ('id',)

admin.site.register(Health, PostAdmin)