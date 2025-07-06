from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.login_page,name='l'),
    path('first/',views.first,name='f'),
     path('register/',views.register,name='r'),
    path('home/',views.ml_p,name='ch'),
    path('dlhome/',views.dl_p,name='dl'),
    path('ai/', views.ai,name='ai'),
    path('aihome/',views.ai_p,name='summarize'),
    path('aiquestion/',views.ai_question,name='question_answering')
]