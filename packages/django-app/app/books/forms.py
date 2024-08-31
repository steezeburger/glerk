from django import forms
from django.forms import HiddenInput

from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'isbn', 'cover_url', 'publication_date', 'author', 'all_data']
        widgets = {
            "all_data": HiddenInput(),
        }
