from django import forms
from .models import Comment


# Define a form for sharing posts via email.
class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)  # Name of the person sharing the post.
    email = forms.EmailField()  # Email address of the person sharing the post.
    to = forms.EmailField()  # Email address of the recipient.
    comments = forms.CharField(required=False, widget=forms.Textarea)  # Optional comments.



# Defines a Django ModelForm for the Comment model.
# A ModelForm is linked directly to a model (Comment) and includes fields specified in the 'fields' list.
# This form will be used to create or update Comment instances from the input provided by users in the web interface.
class CommentForm(forms.ModelForm):
    class Meta:
        # Specifies the model to which this form is linked.
        model = Comment
        # Defines the fields that will be included in the form.
        # This allows users to enter their name, email, and the body of their comment.
        fields = ['name', 'email', 'body']


# Defines a simple form for submitting a search query.
class SearchForm(forms.Form):
    query = forms.CharField()
