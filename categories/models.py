from django.db import models

# Create your models here.


class ListingCategory(models.Model):
    listing_category_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name
