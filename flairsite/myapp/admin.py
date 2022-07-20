from django.contrib import admin
from .models import Health

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phonenumber', 'temperature', 'choise2')

admin.site.register(Health, PostAdmin)