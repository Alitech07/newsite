from django.urls import path
from .views import AboutPage, ArticlePage, index, Serachbar



urlpatterns = [
  path('',index,name='home'),
  path('about/',AboutPage.as_view(),name='about'),
  path('article/<int:pk>/',ArticlePage.as_view(),name='article'),
  path('searchbar/',Serachbar,name='searchbar'),
] 


