from django.contrib import admin
from api.models import User, Tag, Vegetable, Fruit, Company, favouriteFood
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    pass

class TagAdmin(admin.ModelAdmin):
    pass

class VegetableAdmin(admin.ModelAdmin):
    pass

class FruitAdmin(admin.ModelAdmin):
    pass

class CompanyAdmin(admin.ModelAdmin):
    pass

class favouriteFoodAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Vegetable, VegetableAdmin)
admin.site.register(Fruit, FruitAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(favouriteFood, favouriteFoodAdmin)