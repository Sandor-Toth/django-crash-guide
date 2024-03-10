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

# Define the view for displaying a detailed page for a single post.
def post_detail(request, id):
    # Retrieve a single post by ID where the status is 'PUBLISHED'.
    # If no post matches the criteria, raise a 404 error.
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    # Render the detail page for the post using the 'post/detail.html' template.
    # Pass the post to the template context for rendering.
    return render(request, 'blog/post/detail.html', {'post': post})
