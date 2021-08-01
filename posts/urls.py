from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('crp/', views.createPost, name='create_post'),
    path('update_post/<str:pk>/', views.updatePost, name='update_post'),
    path('delete_post/<str:pk>/', views.deletePost, name='delpost'),
] 