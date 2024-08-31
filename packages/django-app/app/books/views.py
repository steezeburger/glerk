from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import BookForm
from .models import Book


@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_book')  # Redirect to a list of books
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})


@login_required
def book_list(request):
    books = Book.objects.all().order_by('-id')
    return render(request, 'book_list.html', {'books': books})

class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('add_book')

def logout_view(request):
    logout(request)
    return redirect('login')
