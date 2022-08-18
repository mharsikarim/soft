from django.contrib import admin
from .models import Category, Services, Cart
from .models import Room, Message

# Register your models here.
class AdmineCategorie(admin.ModelAdmin):
    list_display = ['name']
class AdmineService(admin.ModelAdmin):
    list_display = ('title','category','date_added')
class AdmineCart(admin.ModelAdmin):
    list_display = ('user','service','product_qty','created_at')

admin.site.register(Category,AdmineCategorie)
admin.site.register(Services,AdmineService)
admin.site.register(Cart,AdmineCart)



# Register your models here.
admin.site.register(Room)
admin.site.register(Message)



