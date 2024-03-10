from django.urls import path
from . import views


# Define the application name to use in namespacing of URLs.
app_name = 'blog'

# List of URL patterns for the blog app.
urlpatterns = [
    # URL pattern for the blog post list view.
    # The empty string ('') matches the root URL within the blog app's namespace.
    # 'views.post_list' specifies the view function to handle requests for this URL pattern.
    # 'name='post_list'' names this URL pattern 'post_list' for easy referencing in templates and view functions.
    path('', views.post_list, name='post_list'),

    # URL pattern for the blog post detail view.
    # '<int:id>/' captures a part of the URL as an integer parameter named 'id', which is passed to the view function.
    # This pattern matches URLs like 'blog/1/', where '1' is the ID of the post to display.
    # 'views.post_detail' specifies the view function to handle requests for this URL pattern.
    # 'name='post_detail'' names this URL pattern 'post_detail' for easy referencing.
    path('<int:id>/', views.post_detail, name='post_detail'),
]
