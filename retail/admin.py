from django.contrib import admin

from retail.models import Network, Product


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'supplier', 'debt', 'level',)
    list_filter = ('contacts__city', )
    actions = ['zero_debt']

    def zero_debt(self, request, queryset):
        queryset.update(debt=0.00)

    zero_debt.short_description = 'Обнулить задолженность'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = "__all__"
