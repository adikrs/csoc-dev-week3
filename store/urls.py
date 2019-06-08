from django.urls import path
from store.views import *


urlpatterns = [
    path('',index,name="index"),
    path('books/',bookListView,name="book-list"),
    path('book/<int:bid>/',bookDetailView,name='book-detail' ),
    path('books/loaned/',viewLoanedBooks,name="view-loaned"),
    path('books/loan/',loanBookView,name="loan-book"),
    path('books/return',returnBookView,name="return-book"), #copy the path and change index
    path('books/rating',rating_bookView,name="rating-book")
]


