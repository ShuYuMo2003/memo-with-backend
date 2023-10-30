from django.db import models

# Create your models here.
GENDER_TYPE = [
    ("M", "Male"),
    ("F", "Female"),
    ("TW", "Transgender Woman"),
    ("TM", "Transgender Man")
]

class Person(models.Model):
    name                = models.TextField(max_length=100)
    birthdate           = models.DateTimeField(blank=True, null=True)
    photos_uuid         = models.JSONField(blank=True, null=True)
    gender              = models.CharField(choices=GENDER_TYPE, blank=True, null=True, max_length=5)

    lost_place          = models.TextField(blank=True, null=True)
    lost_date           = models.DateField(blank=True, null=True)

    family_name         = models.TextField(blank=True, null=True)
    family_phone        = models.TextField(blank=True, null=True)
    family_email        = models.TextField(blank=True, null=True)
    family_address      = models.TextField(blank=True, null=True)



