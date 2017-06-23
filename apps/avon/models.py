from django.db import models

# Create your models here.

class Campaing(models.Model):
	name = models.CharField(max_length=50)
	campaing_num=models.PositiveIntegerField(default=0)
	deperture_date = models.DateField(null=True)
	arrival_date = models.DateField(null=True)
	def __str__(self):
		return self.name




class Customer(models.Model):
	name = models.CharField(max_length=50)
	debt = models.PositiveIntegerField(default=0,blank=True)
	class Meta:
		ordering=['debt']
	def __str__(self):
		return self.name

class Article(models.Model):
	CATEGORY_CHOICES=(
		('PYC','Perfumería y cosméticos'),
		('RYH','Ropa y del hogar'),
	)
	campaing=models.ForeignKey(Campaing,on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	price = models.PositiveIntegerField(default=0)
	category = models.CharField(max_length=5,choices=CATEGORY_CHOICES)
	buyer = models.ManyToManyField(Customer)

	class Meta:
		ordering=['name']


	def get_percent(self):
		return 30 if category == 'PYC' else 20
	def __str__(self):
		return self.name
