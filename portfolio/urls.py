from django.urls import path
from . import views

urlpatterns = [
   path('posts/', views.lista_posts, name='lista_posts'),
    path('novo/', views.criar_post, name='criar_post'),
    path('contato/', views.contato, name='contato'),
    path('contato/sucesso/', views.contato_sucesso, name='contato_sucesso'),
]



