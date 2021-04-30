from django.contrib import admin
from .models import Movie
# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id','name','description')
    list_display_links = ('id','name')
    list_filter =('created_date',)
#register your models here.add()

admin.site.register(Movie,MovieAdmin)