from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('animes/', views.anime, name='animes'),
    path('adicione/', views.adicione, name='adicione'),
    path('listanimes/', views.lista_animes, name='lista_animes'),
    path('animes/<int:anime_id>/', views.detalhe_anime, name='detalhe_anime'),
    path('sucesso/', views.sucesso, name='sucesso'),  # Adicione esta linha para a página de sucesso
]
