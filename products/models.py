from django.db import models

# Create your models here.


class Product(models.Model):
    """Model definition for Product."""

    title = models.CharField(max_length=250, blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    description = models.TextField(blank=True)
    summary = models.TextField(blank=True, null=True)
    featured = models.BooleanField(default=True)

    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        """Unicode representation of Product."""
        return (self.title)+" ( $ " + str(self.price) + ")"
