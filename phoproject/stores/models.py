from django.db import models
from django.core.validators import RegexValidator
# Create your models here.


class PhoPlace(models.Model):
    pho_name = models.CharField(max_length=200, blank=False)
    street = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True)
    zip_code = models.IntegerField(blank=True, default=0)
    website = models.CharField(max_length=430, blank=True)
    phoneNumber = models.CharField(validators=[RegexValidator(r'\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4} |\(\d{3}\)\s *\d{3}[-\.\s]??\d{4} |\d{3}[-\.\s]??\d{4}')
                                               ], max_length=10, blank=True)
    description = models.TextField(blank=True)
    logo_image = models.ImageField(
        upload_to="phoImages", blank=True, default="")
    email = models.EmailField(max_length=245, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.pho_name},{self.city}"
