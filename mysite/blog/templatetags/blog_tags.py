from django import template
from ..models import Post
from django.db.models import Count

# Initialize the template library.
register = template.Library()

# A simple tag returning the total number of published posts.
@register.simple_tag
def total_posts():
    return Post.published.count()

# An inclusion tag that renders a template with the latest posts.
# 'count' defaults to 5 if not specified.
@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}

# A simple tag that returns the most commented posts, ordered by the number of comments.
@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(
               total_comments=Count('comments')
           ).order_by('-total_comments')[:count]
