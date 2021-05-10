from django.contrib import admin
from .models import OrderModels


class OrderModelsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in OrderModels._meta.fields]

    class Meta:
        model = OrderModels


admin.site.register(OrderModels, OrderModelsAdmin)