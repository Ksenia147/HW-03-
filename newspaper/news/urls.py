from django.urls import path
from .views import PostList, PostDetail, PostSearch, PostCreate, PostUpdate, PostDelete



urlpatterns = [
   path('', PostList.as_view(), name='post_list'),
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('search', PostSearch.as_view()),
   path('create/', PostCreate.as_view()),
   path('articles/create/', PostCreate.as_view()),
   path('<int:pk>/edit/', PostUpdate.as_view()),
   path('articles/<int:pk>/edit/', PostUpdate.as_view()),
   path('<int:pk>/delete/', PostDelete.as_view()),
   path('articles/<int:pk>/delete/', PostDelete.as_view()),



]