# Import necessary Django modules and the Post model from the current app's models.
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Post

# Define the view for displaying a list of posts.
def post_list(request):
    # Retrieve all published posts using the custom 'published' manager defined in the Post model.
    posts = Post.published.all()
    # Render the list of posts using the 'post/list.html' template.
    # Pass the list of posts to the template context for rendering.
    return render(request, 'blog/post/list.html', {'posts': posts})

# Defines the view function for displaying the detail of a single post.
# The function takes 'year', 'month', 'day', and 'post' (slug) as parameters from the URL.
# These parameters are used to find a specific post that matches all the given criteria:
# 1. The post must have a status of 'PUBLISHED'.
# 2. The post's slug must match the 'post' parameter.
# 3. The post's publication date must match the 'year', 'month', and 'day' parameters.
# If no post matches these criteria, a 404 page is displayed.
# If a post is found, it renders the 'blog/post/detail.html' template,
# passing the post object to the template context for display.
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})
