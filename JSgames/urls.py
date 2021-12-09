from django.urls import path
from JSgames.views import chessGame
app_name="JSgames"
urlpatterns=[
    path('chessGame',chessGame,name="chessGame"),
]