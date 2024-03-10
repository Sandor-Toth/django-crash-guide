from django import forms


# Define a form for sharing posts via email.
class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)  # Name of the person sharing the post.
    email = forms.EmailField()  # Email address of the person sharing the post.
    to = forms.EmailField()  # Email address of the recipient.
    comments = forms.CharField(required=False, widget=forms.Textarea)  # Optional comments.
