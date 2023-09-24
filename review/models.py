from djongo import models
from django.core.validators import MinValueValidator, MaxValueValidator

from store.models import StoreModel
from user.models import User

# Create your models here.
class Review(models.Model):
    _id = models.ObjectIdField()

    review_of = models.ForeignKey(
        StoreModel, 
        on_delete=models.CASCADE, 
        related_name="reviews"
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    review = models.TextField(null=False)
    score = models.FloatField(
        null=False, 
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )

