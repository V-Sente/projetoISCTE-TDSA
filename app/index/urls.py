from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

# Create your urls here.


urlpatterns = [
    path('', index, name='index'),
    path('cadastrar_usuario/', cadastrar_usuario, name='cadastrar_usuario'),
    path('cadastrar_criador/', cadastrar_criador, name='cadastrar_criador'),
    path('logar_usuario/', logar_usuario, name='logar_usuario'),
    path('dashboard/', dashboard, name='dashboard'),
    path('deslogar_usuario/', deslogar_usuario, name='deslogar_usuario'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)