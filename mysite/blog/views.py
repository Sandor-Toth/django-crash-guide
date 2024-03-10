# Import necessary Django modules and the Post model from the current app's models.
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator
from django.views.generic import ListView


# This class defines an alternative list view for blog posts using Django's generic ListView.
# ListView is a powerful generic view provided by Django for displaying a list of objects.
class PostListView(ListView):
    """
    Alternative post list view.
    """
    # Specifies the queryset that will be used to retrieve objects.
    # Here, it uses the custom 'published' manager to fetch all published posts.
    queryset = Post.published.all()

    # Sets the name of the context variable to be used in the template to access the list of posts.
    # By default, ListView uses 'object_list', but specifying 'posts' makes the template code clearer.
    context_object_name = 'posts'

    # Enables pagination for the view, specifying the number of posts to display per page.
    paginate_by = 3

    # Defines the path to the template used to render the list view.
    # By default, ListView uses the <app_name>/<model_name>_list.html template.
    template_name = 'blog/post/list.html'
    

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
