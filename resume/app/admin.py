from django.contrib import admin
from .models import Resume
admin.site.register(Resume)

# Register your models here.
class ResumeAdmin(admin.ModelAdmin):
    list_display=('name','phone','email','educaton','experience','skills','languages','projects','state','city','block','house_number')
