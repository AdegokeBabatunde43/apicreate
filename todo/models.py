from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price= models.IntegerField()
    quantity= models.IntegerField()
    ImageUrl1=models.URLField(blank=True)
    ImageUrl2=models.URLField(blank=True)
    ImageUrl3=models.URLField(blank=True)
    ImageUrl4=models.URLField(blank=True)
    ImageUrl5=models.URLField(blank=True)
    status=models.BooleanField(blank=True)
    DateTimeField=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
        
