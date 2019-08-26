from django.db import models


# Create your models here.
class Product(models.Model):
	pid = models.IntegerField()
	name = models.CharField(max_length=200)
	price = models.IntegerField()
	description = models.CharField(max_length=200)


class Machine(models.Model):
	Mid = models.CharField(max_length=100)
	location = models.CharField(max_length=200)
	active_template = models.CharField(max_length=200)


class Payments(models.Model):
	transactionid = models.CharField(max_length=1000)
	product = models.ManyToManyField(Product)


class Users(models.Model):
	Name = models.CharField(max_length=100)
	designation = models.CharField(max_length=100)
	Inprod = models.ManyToManyField(Product, related_name="Inprod")
	OutProd = models.ManyToManyField(Product, related_name="Outprod")

