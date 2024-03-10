# Django Blog Application

This Django application provides a comprehensive blogging platform, featuring post listing, post detail views with comments, email sharing of posts, tag-based filtering, similar posts recommendations, and a search functionality.

## Features

- **Post Listing**: Utilize Django's `ListView` to display all published blog posts, with support for pagination.
- **Tag Filtering**: Filter blog posts by tags to narrow down the list to specific topics of interest.
- **Post Detail View**: Detailed view for each post, including the post content, comments, and similar post recommendations based on shared tags.
- **Comments System**: Allow readers to leave comments on posts, enhancing engagement and interaction.
- **Email Sharing**: Enable users to share posts via email, including a personalized message.
- **Search Functionality**: Implement full-text search allowing users to find posts containing specific terms.

## Key Components

### Views

- `PostListView`: Alternative view for listing posts with pagination.
- `post_list`: Function view to display posts, with optional tag filtering.
- `post_detail`: Shows detailed information for a specific post, including comments and similar posts.
- `post_share`: Handles the form submission for sharing a post via email.
- `post_comment`: Processes adding new comments to a post.
- `post_search`: Implements search functionality using PostgreSQL's full-text search capabilities.

### Models

- `Post`: Represents blog posts, including fields for title, slug, author, and body, among others.
- `Comment`: Represents comments made on blog posts.

### Forms

- `EmailPostForm`: Form used for sharing posts via email.
- `CommentForm`: Form for submitting comments on posts.
- `SearchForm`: Form to capture user search queries.

### Templates

- Post list and detail templates, including pagination and dynamic content for tags and similar posts.
- Comment and search forms, and handling of form submissions with appropriate feedback to the user.

## Dependencies

- Django
- PostgreSQL (for full-text search and Trigram similarity)
- `django-taggit` (for tagging functionality)

## Setup

1. Install required packages: `pip install -r requirements.txt`
2. Apply migrations: `python manage.py migrate`
3. Run the development server: `python manage.py runserver`
4. Access the application at `http://127.0.0.1:8000`.

## Contributing

Contributions to enhance functionalities or documentation are welcome. Please fork the repository and submit a pull request with your changes.