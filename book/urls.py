from django.urls import path
from .views import *
urlpatterns=[
    path('List/', book_list,name='book_list'),
    path('Add/', book_add,name='book_add'),
    path('/<str:name>', book_details,name='book_details'),
    path('Update/<id>/', book_update,name='book_update'),
    path('Delete/<int:id>/', book_delete,name='book_delete'),

]