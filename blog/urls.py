from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, user_logout, LikeView, AboutView


urlpatterns = [
    
    path('', HomeView, name='index'),
    path('detail/<int:id>/', ArticleDetailView, name='detail'),
    path('add_post', AddPostView, name='add_post'),
    path('update_post/<int:pk>/', UpdatePostView.as_view(), name='update_post'),
    path('delete_post/<int:pk>/', DeletePostView.as_view(), name='delete_post'),
    path('logout/', user_logout, name='logout' ),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('about/', AboutView.as_view(), name='about'),
]