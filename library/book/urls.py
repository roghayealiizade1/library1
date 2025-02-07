from django.urls import path 
from . import views

urlpatterns = [
    path('library/<id>',views.library),
    path('book_list',views.book_list),
    path('detail/<int:id>',views.detail,name='book_list'),
    path('random/<number>',views.random),
    path('detail2',views.detail2)
]