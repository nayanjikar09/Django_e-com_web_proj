from django.db import models

class Product(models.Model):
    product_id = models.AutoField # Corrected AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300, default="")  # Added default=""
    pub_date = models.DateField(null=True, blank=True)  # Allows null values
    image = models.ImageField(upload_to="Shop/images", default="")

    def __str__(self):
        return self.product_name  # Should work fine now
