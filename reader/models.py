from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


# Create your models here.
class Reader(models.Model):
    phone_regex = RegexValidator(regex=r'^(0[0-9]{1,2}-[0-9]{6,6})|([0-9]{10})$', message="Phone number must be entered in the format: '000-555555' or '+999-9999999999'.")

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=255, validators=[phone_regex], null=True, blank=True, help_text="Phone number must be entered in the format: '000-555555' or '+999-9999999999'.")
    image = models.ImageField(upload_to="images/reader/", null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    dob = models.DateField(null=True, blank=True, help_text="write in 2010-01-01")
    is_author = models.BooleanField(default=False)
    keywords = models.TextField(null=True, blank=True, help_text="write in keyword1, keyword2, format")

    class Meta:
        verbose_name_plural = "readers"

    def __str__(self):
        return str(self.user.username)
