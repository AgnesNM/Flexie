from django.db import models

# Create your models here.

class FlexieUsers(models.Model):
    email = models.EmailField(max_length=254)
    username = models.CharField(max_length=254, default = 'scraper_users')     
    # password = models.CharField(widget=models.PasswordInput)

    def __str__(self):
        return self.username
