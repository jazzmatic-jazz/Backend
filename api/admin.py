from django.contrib import admin
from .models import Note, UserManager, User

admin.site.register(Note)
admin.site.register(User)