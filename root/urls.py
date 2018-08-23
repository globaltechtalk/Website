from django.urls import path
from root import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('pastmeetups/', views.pastmeetups),
    path('contact/', views.contact),
    path('index/', views.home),
    path('sponsors/', views.sponsor),
    path('upcomingmeetups/', views.ucmp),
    path('communitypartners/', views.community_partners),
]
