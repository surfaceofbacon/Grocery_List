from django.db import models

# Create your models here.

class GroceryEntry(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(blank=True, default=1)
    purchased = models.BooleanField(blank=True, default=False)
    importance_color_choices = {
        'G': 'Green',
        'Y': 'Yellow',
        'R': 'Red',
    }
    importance_color = models.CharField(max_length=5, choices=importance_color_choices, blank=True, default='G')
    unit = models.CharField(max_length=50, blank=True, null=True)
    brand = models.CharField(max_length=50, blank=True, null=True)
    store = models.CharField(max_length=50, blank=True, null=True)

    def __repr__(self):
        return f'{self.quantity} {self.name}'

    def __str__(self):
        return f'{self.quantity} {self.name}'
