from django.urls import path
from .views import homeNews,ArticoloDetailViewCB,ArticoloListView,GiornalistaListView,GiornalistaDetailViewCB #articoloDetailView

app_name="news"

urlpatterns = [
    path('',homeNews,name="homeNews"),
    #path('articoli/<int:pk>',articoloDetailView,name='articolo_detail'),
    path("articoli/<int:pk>",ArticoloDetailViewCB.as_view(),name="articolo_detail"),
    path('lista_articoli/',ArticoloListView.as_view(),name='lista_articoli'),
    path('lista_giornalisti/',GiornalistaListView.as_view(),name='lista_giornalisti'),
    path('gionalisti/<int:pk>',GiornalistaDetailViewCB.as_view(),name="giornalista_detail")
]
