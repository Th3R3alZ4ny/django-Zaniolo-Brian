from django.urls import path
from prima_app.views import homepage
from prima_app.views import welcome
from prima_app.views import lista

app_name="prima_app"
urlpatterns=[
    path('',homepage,name="homepage"),
    path('welcome',welcome,name="welcome"),
    path('lista',lista,name="lista"),
]