from django.db import models


# Create your models here.
class HomePage(models.Model):
    site_name = models.CharField(max_length=255)
    site_tagline = models.TextField()

    def create(self):
        self.save()

    # Please rename to something sensible
    @property
    def full_site_info(self):
        return "{}{}".format(self.site_name, self.site_tagline)

    def __str__(self):
        return f"{self.site_name} {self.site_tagline}"
