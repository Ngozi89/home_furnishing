from django.core.validators import MinLengthValidator
from django.db import models

from django.contrib.auth.models import User
from products.models import Product


class Review(models.Model):
    """
    Model for a review on a product.
    """
    products = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, null=False, blank=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField(
        validators=[MinLengthValidator(
            20, "Review must be greater than 20 words")],
        max_length=500
    )
    rating = models.IntegerField()

    helpful_votes = models.ManyToManyField(
        User, related_name='helpful_votes', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [['products', 'user']]
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_helpful_votes(self):
        return self.helpful_votes.count()
