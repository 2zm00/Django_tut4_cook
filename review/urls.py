from django.urls import path
from . import views

app_name = 'review'

urlpatterns = [
    path('', views.review_index, name='review_index'),
    path('<int:pk>/', views.review_detail, name='review_detail'),
    path('create/', views.review_create, name='review_create'),
]