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

    # Defines a URL pattern for the post_detail view that includes year, month, day, and a slug in the URL.
    # The pattern captures four keyword arguments: 'year', 'month', 'day', and 'post' (the slug of the post),
    # which are passed to the post_detail view function.
    # This allows for URLs that include the publication date of the post and its slug, 
    # making the URL descriptive and SEO-friendly.
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),

]
