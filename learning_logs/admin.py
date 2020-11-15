from django.contrib import admin

# Register your models here.
from .models import Menu, Menu_item, Row, Seat, Section, Topic, Entry

admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(Section)
admin.site.register(Row)
admin.site.register(Seat)
admin.site.register(Menu)
admin.site.register(Menu_item)
