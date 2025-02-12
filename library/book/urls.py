from django.urls import path 
from . import views

urlpatterns = [
    path('library/<id>',views.library),
    path('standard_book_list',views.standard_book_list,name='standard_book_list'),
    path('detail/<int:id>',views.detail,name='detail'),
    path('detail2',views.detail2)
    
]