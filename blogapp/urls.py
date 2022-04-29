from django.urls import path
from . import views   
from .views import HomeView, ArticleDetailView, AddPostView



urlpatterns = [
    path('' , views.main, name='main_page'),  
    path('home/' , HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    
]