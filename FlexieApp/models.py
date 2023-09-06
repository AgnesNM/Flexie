from django.db import models

class FlexieUsers(models.Model):
    email = models.EmailField(max_length=254)
    username = models.CharField(max_length=254, default = 'scraper_users')     
    upload_file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

