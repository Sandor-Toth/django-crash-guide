from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    slug = models.SlugField(max_length=250)  # URL slug for the post
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
