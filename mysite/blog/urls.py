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

    # path('', views.PostListView.as_view(), name='post_list'),

    # Defines a URL pattern for the post_detail view that includes year, month, day, and a slug in the URL.
    # The pattern captures four keyword arguments: 'year', 'month', 'day', and 'post' (the slug of the post),
    # which are passed to the post_detail view function.
    # This allows for URLs that include the publication date of the post and its slug, 
    # making the URL descriptive and SEO-friendly.
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),

    # URL pattern for the "share" functionality of a post.
    # It captures the post's ID from the URL and passes it to the post_share view.
    path('<int:post_id>/share/', views.post_share, name='post_share'),

    # URL pattern for adding a comment to a post. 
    # The pattern captures the post's ID and routes the request to the post_comment view.
    path('<int:post_id>/comment/', views.post_comment, name='post_comment'),

    # Defines a URL pattern for filtering blog posts by tags.
    # The pattern captures a slug (tag_slug) representing a specific tag and passes it to the post_list view.
    # This allows the URL to be descriptive, indicating that it filters posts by a given tag.
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),

    # URL pattern that routes requests to the 'post_search' view for post searching.
    path('search/', views.post_search, name='post_search'),

]
