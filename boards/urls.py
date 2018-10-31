from django.urls import path
from . import views

urlpatterns = [
    #path('',views.home,name='board_topics')
    path('',views.home.as_view()),name='board_topics'),
]
