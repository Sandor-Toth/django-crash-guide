# Import necessary Django modules and the Post model from the current app's models.
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.core.paginator import Paginator
from django.views.generic import ListView
from .forms import EmailPostForm, CommentForm
from django.core.mail import send_mail
from django.views.decorators.http import require_POST


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


def post_detail(request, year, month, day, post):
    # Fetch the post based on URL parameters and ensure it is published.
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED, slug=post,
                             publish__year=year, publish__month=month, publish__day=day)
    # Retrieve active comments for the post.
    comments = post.comments.filter(active=True)
    # Instantiate the form for adding comments.
    form = CommentForm()
    # Render the post detail template with the post, comments, and form included in the context.
    return render(request, 'blog/post/detail.html', {'post': post, 'comments': comments, 'form': form})


def post_share(request, post_id):
    # Retrieve the post by ID only if it's published; otherwise, raise a 404 error.
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    sent = False  # Flag to indicate if the email has been sent.
    if request.method == 'POST':
        # The form was submitted.
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # All form fields passed validation.
            cd = form.cleaned_data
            # Build the absolute URL of the post.
            post_url = request.build_absolute_uri(post.get_absolute_url())
            # Create the email subject and message.
            subject = f"{cd['name']} recommends you read {post.title}"
            message = f"Read {post.title} at {post_url}\n\n" \
                      f"{cd['name']}'s comments: {cd['comments']}"
            # Send the email.
            send_mail(subject, message, 'your_account@gmail.com', [cd['to']])
            sent = True  # Update the flag.
    else:
        # Initialize an empty form instance to display the form in GET request.
        form = EmailPostForm()
    # Render the share template with the context variables: post, form, and sent flag.
    return render(request, 'blog/post/share.html', {'post': post, 'form': form, 'sent': sent})


@require_POST  # This decorator ensures the view only handles POST requests.
def post_comment(request, post_id):
    # Retrieve the post by ID and ensure it is published.
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = None  # Initialize the comment variable.
    # Instantiate the form with POST data.
    form = CommentForm(data=request.POST)
    if form.is_valid():
        # Create a Comment object but don't save to the database yet.
        comment = form.save(commit=False)
        # Assign the current post to the comment.
        comment.post = post
        # Now save the comment to the database.
        comment.save()
    # Render a template specifically for handling the comment submission.
    # Pass the post, form, and potentially the newly created comment to the context.
    return render(request, 'blog/post/comment.html', {'post': post, 'form': form, 'comment': comment})


