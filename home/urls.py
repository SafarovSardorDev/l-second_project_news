from django.urls import path
from .views import (addnewsview, list,
                    contactpage,tags ,
                    SearchView,# OwnProfilePage,
                    categorypage,translatepage,
                    NewsDetailView, 
                    NewsDeleteView,
                    NewsUpdateView)
#app_name = "news"
urlpatterns = [
    #path('' , HomePage.as_view() , name='home'),
    # path('', HomePage2, name="home"),
    path('', categorypage, name ='home' ),
    path('add_new/', addnewsview, name='add_new'),
    path('contact/' , contactpage , name='contact'),
    path('search/'  , SearchView.as_view() , name ='search'),
    path("news<int:pk>" , NewsDetailView.as_view() , name ='news_detail'),
    path('<int:pk>/delete/' , NewsDeleteView.as_view(), name ='news_delete'),
    path('<int:pk>/update/', NewsUpdateView.as_view() , name='news_update' ),
    path('category_sort/', list, name="category_sort"),
    path('tags_sort/', tags, name="tags_sort"),
    #path('profile/', OwnProfilePage.as_view() , name='profile_page' )
    path('translate/', translatepage, name='translate')
    
    
]