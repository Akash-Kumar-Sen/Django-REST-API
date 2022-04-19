from django.contrib import admin
from .models import BoxItem,RestrictionModel
# Register your models here.

class RestrictionModelAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() > 0:
            return False
        else:
            return True


admin.site.register(BoxItem)
admin.site.register(RestrictionModel, RestrictionModelAdmin)