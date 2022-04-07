from django.urls.conf import path
from django.urls import path
from prova_pratica_1.views import view_b,view_c,lista_materie,json_version

app_name="prova_pratica_1"
urlpatterns = [
    path('view_b',view_b,name="view_b"),
    path('view_c',view_c,name="view_c"),
    path('lista_materie',lista_materie,name="lista_materie"),
    path('json_version',json_version,name="json_version"),
]