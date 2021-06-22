from django.urls import path

from . import views

urlpatterns = [
    path('', views.root),
    path('guess', views.guess),
    path('reset', views.reset),
    # path('leaderboard', views.leader),
    
]
