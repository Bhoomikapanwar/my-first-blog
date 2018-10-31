from django.urls import path
from boards import views

urlpatterns = [
    path('/boards',views.board_topics,name='board_topics'),
]
