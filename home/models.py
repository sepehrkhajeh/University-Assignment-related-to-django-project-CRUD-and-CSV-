from django.db import models

# Create your models here.

class UploadFileModel(models.Model):
    file = models.FileField(upload_to='file/')
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        if self.file:
            return self.file.path
        else:
            return None
        
    def path(self):
        return self.file.path
    
    
    
class FashionRetailSales(models.Model):
    Customer = models.CharField(max_length=255,verbose_name='Customer Reference ID')
    item = models.CharField(max_length=255,verbose_name='Item Purchased')
    amount = models.FloatField(verbose_name='Purchase Amount (USD)',blank=True,null=True)
    date_purchased = models.CharField(verbose_name='Date Purchase',max_length=255)
    Review_Rating = models.CharField(max_length=255,verbose_name='Review Rating')
    Payment_Method = models.CharField(max_length=255,verbose_name='Payment Method')
    
    class Meta:
        ordering = ('-id',)
    def __str__(self):
        return self.item