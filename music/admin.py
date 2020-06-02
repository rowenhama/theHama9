from django.contrib import admin
from .models import Album, Song


#register the Album class on the admin site(app kinda kkk)
admin.site.register(Album)
#register the Song class (app) on the admin side
admin.site.register(Song)
