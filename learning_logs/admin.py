from django.contrib import admin
from .models import Topic,Entry,Entr, Blog, Author
admin.site.register(Topic)
admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Entr)
admin.site.register(Entry)
# Register your models here.
