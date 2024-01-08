from django.contrib.auth import get_user_model
from django.db import models

user_model = get_user_model()


class Story(models.Model):
    products = models.TextField()
    user = models.ForeignKey(to=user_model, on_delete=models.CASCADE)
    recipe = models.TextField()
