from django.contrib import admin
from .models import UploadFileModel,FashionRetailSales


# Register your models here.

class UploadFileAdmin(admin.ModelAdmin):
    
    
    class Meta:
        model = UploadFileModel
        
    
class FashionRetailSalesAdmin(admin.ModelAdmin):
    
    class Meta:
        model= FashionRetailSales
        
admin.site.register(UploadFileModel, UploadFileAdmin)
admin.site.register(FashionRetailSales, FashionRetailSalesAdmin)