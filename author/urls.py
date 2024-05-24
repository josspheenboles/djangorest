from django.urls import path
from .views import *

urlpatterns = [
    path('/', author_list),
    path('<int:pk>/', author_detail),
    path('authorsgeneric/', AuthorListCreate.as_view(), name='author-list-create'),
    path('authorsgeneric/<int:pk>/', AuthorRetrieveUpdateDestroy.as_view(), name='author-detail'), path('authors/', AuthorListCreate.as_view(), name='author-list-create'),
    path('authorsgeneric/<int:pk>/', AuthorRetrieveUpdateDestroy.as_view(), name='author-detail'),
]
