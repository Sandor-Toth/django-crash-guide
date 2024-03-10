from django.contrib import admin
from .models import Profile

# Registering the Profile model with the Django admin site using a decorator.
# This allows the Profile model to be managed through the Django admin interface.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # Customizing the display of profiles in the admin list view. 
    # Shows the 'user', 'date_of_birth', and 'photo' fields.
    list_display = ['user', 'date_of_birth', 'photo']
    
    # Use a raw ID widget for the 'user' field instead of a dropdown.
    # Useful for sites with a large number of user instances.
    raw_id_fields = ['user']
