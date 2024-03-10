from django.db import models
from django.conf import settings

# Defines a Profile model linked to the Django User model with additional fields.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    # String representation of the model, useful for debugging and in the Django admin.
    def __str__(self):
        return f'Profile of {self.user.username}'
