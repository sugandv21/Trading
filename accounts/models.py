from django.db import models

class SiteAsset(models.Model):
    key = models.CharField(max_length=50, unique=True)  
    image = models.ImageField(upload_to="site_assets/")

    def __str__(self):
        return self.key
