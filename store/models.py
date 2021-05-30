from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    category_description = models.CharField(max_length=100)
    category_image = models.ImageField(blank=True)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_description = models.CharField(max_length=100)
    product_price = models.IntegerField()
    product_total = models.IntegerField(default=20000)
    product_image = models.ImageField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

    def display_price(self):
        price_with_vat = self.product_price * 1.25
        display_price = price_with_vat/100

        return display_price
