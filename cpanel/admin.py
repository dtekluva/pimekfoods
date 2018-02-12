from django.contrib import admin
from store.models import Product, Customers, Messages
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name', 'price','slug',)
    

class MessagesAdmin(admin.ModelAdmin):

    list_display = ('message',)

# class UserAdmin(admin.ModelAdmin):

#     list_display = ('title', 'product', 'backs', 'pub_date')



admin.site.register(Product, ProductAdmin)
admin.site.register(Messages, MessagesAdmin)