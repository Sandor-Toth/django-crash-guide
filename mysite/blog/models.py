from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Custom manager for querying published posts.
class PublishedManager(models.Manager):
    def get_queryset(self):
        # Calls the superclass's get_queryset method and filters posts by the 'PUBLISHED' status.
        return super().get_queryset()\
                      .filter(status=Post.Status.PUBLISHED)

# Defines the Post model.
class Post(models.Model):
    
    # Nested Status class to define Post status choices.
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'      # Draft status
        PUBLISHED = 'PB', 'Published'  # Published status

    # Model fields
    title = models.CharField(max_length=250)  # Title of the post
    # By using unique_for_date, the slug field is now required to be unique for the date stored in the publish field.
    slug = models.SlugField(max_length=250, unique_for_date='publish')  # URL slug for the post
    # Add many-to-one relationship
    author = models.ForeignKey(User,  # Link to the user who authored the post
                               on_delete=models.CASCADE,  # Deletes post if user is deleted
                               related_name='blog_posts')  # Name to use for the reverse relation from User to Post
    body = models.TextField()  # Body of the post
    publish = models.DateTimeField(default=timezone.now)  # Publication datetime
    created = models.DateTimeField(auto_now_add=True)  # Datetime of creation, set only once
    updated = models.DateTimeField(auto_now=True)  # Datetime of last update, updated on save
    status = models.CharField(max_length=2,  # Post status, uses the Status choices
                              choices=Status.choices,
                              default=Status.DRAFT)

    # Model managers
    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager for published posts.

    # Meta options for the Post model
    class Meta:
        ordering = ['-publish']  # Default ordering of posts by descending publication date
        indexes = [
            models.Index(fields=['-publish']),  # Index to improve query performance on 'publish' field
        ]

    # String representation of the Post model
    def __str__(self):
        return self.title  # Returns the post title
    
    # Defines a method to construct the absolute URL for a specific instance of a post.
    # This method utilizes Django's 'reverse' function to dynamically generate the URL path.
    # The 'reverse' function is called with the name of the URL pattern ('blog:post_detail') and
    # a list of arguments that correspond to the URL pattern's dynamic segments.
    # These arguments are the year, month, day of the post's publication date, and the post's slug,
    # allowing the method to create a URL that uniquely identifies the post by its publication date and slug.
    # This absolute URL is used for accessing the post directly via a web browser.
    def get_absolute_url(self):
        return reverse('blog:post_detail',
                    args=[self.publish.year,
                            self.publish.month,
                            self.publish.day,
                            self.slug])


