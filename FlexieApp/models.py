from django.db import models

class FlexieUsers(models.Model):
    email = models.EmailField(max_length=254, null=True, verbose_name="")
    upload_file = models.FileField(upload_to='uploads/', null=True, verbose_name="")

    def __str__(self):
        return self.email
