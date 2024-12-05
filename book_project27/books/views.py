from django.http import HttpResponseNotFound
from .models import Category, Book

def home(request):
    categories = Category.objects.all()
    books = Book.objects.all()
    return render(request, 'home.html', {'categories': categories, 'books': books})

def books_by_category(request, category_id):
    category = Category.objects.filter(id=category_id).first()
    if not category:
        return HttpResponseNotFound("Kategoriya topilmadi!")
    books = category.book_set.all()
    return render(request, 'books_by_category.html', {'category': category, 'books': books})

def book_detail(request, book_id):
    book = Book.objects.filter(id=book_id).first()
    if not book:
        return HttpResponseNotFound("Kitob topilmadi!")
    return render(request, 'book_detail.html', {'book': book})
