from django.db import models

# Create your models here.
class Categories(models.Model):
    catagorie=models.CharField(max_length=100)
class SubCatagories(models.Model):
    #question = models.ForeignKey(Question, on_delete=models.CASCADE)
    subCatagories=models.CharField(max_length=100)
class Products(models.Model):
    #question = models.ForeignKey(Question, on_delete=models.CASCADE)
    products=models.CharField(max_length=100)




