# Import the admin module from Django's admin interface and the Post model from the current app's models.
from django.contrib import admin
from .models import Post, Comment

# This decorator registers the Post model with the admin site,
# and the class below customizes the admin interface for the Post model.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # list_display controls which fields are displayed on the change list page of the admin.
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    
    # list_filter adds a sidebar that lets you filter the change list by the specified fields.
    list_filter = ['status', 'created', 'publish', 'author']
    
    # search_fields adds a search box at the top of the change list. When someone enters search terms,
    # Django will search the specified fields.
    search_fields = ['title', 'body']
    
    # prepopulated_fields specifies fields where the value is automatically set using the value of other fields.
    # Here, the 'slug' field is filled in with the input of the 'title' field, using a slugified version.
    prepopulated_fields = {'slug': ('title',)}
    
    # raw_id_fields replaces the default drop-down for selecting related objects with a lookup widget.
    # This is useful for fields with many choices, like 'author', to improve usability.
    raw_id_fields = ['author']
    
    # date_hierarchy adds navigation links to navigate through a date hierarchy. This allows quick filtering
    # by 'publish' dates.
    date_hierarchy = 'publish'
    
    # ordering sets the default ordering for the change list in the admin. This is applied when no other
    # order is specified.
    ordering = ['status', 'publish']


# Registers the Comment model with the Django admin, customizing the admin interface.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # Customizes the display list in the admin interface to include relevant fields.
    list_display = ['name', 'email', 'post', 'created', 'active']
    # Adds filters to the sidebar for easier navigation through comments.
    list_filter = ['active', 'created', 'updated']
    # Enables search functionality for comment properties.
    search_fields = ['name', 'email', 'body']
