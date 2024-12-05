from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:category_id>/', views.books_by_category, name='books_by_category'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
]
