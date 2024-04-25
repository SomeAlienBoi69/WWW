from django.db import models

class Seller(models.Model):
    Name = models.CharField(max_length=50)
    PhoneNumber = models.IntegerField()



class Product(models.Model):
    Name = models.CharField(max_length=50)
    Price = models.DecimalField(max_digits=10,decimal_places=2 )
    Description = models.CharField(max_length=500)
    SellerID = models.ForeignKey(Seller, on_delete=models.SET_NULL, null = True)
    Image_url = models.CharField(max_length=256, null=True, blank=True, default="https://i.imgur.com/XKAFJmx.png")
    def __str__(self):
        return f'{self.Name} {self.Price} {self.Description} {self.Image_url}'

class Client(models.Model):
    Name = models.CharField(max_length=50)
    PhoneNumber = models.IntegerField()
    Adress = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.name}'