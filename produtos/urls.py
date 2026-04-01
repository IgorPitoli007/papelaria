from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'produtos' 

urlpatterns=[
    path('', views.home_produtos, name='home'),
    path('ver_produtos/', views.ver_produtos, name='ver_produtos'),
    path('criar_produtos/', views.criar_produtos, name='criar_produtos'),
    path('login/', views.login, name="login"),    
    path('criar/', views.criar, name='criar'),
    path('deletar/<int:id>/', views.deletar, name='deletar'),
    path('editar_produtos/<int:id>/', views.editar_produtos, name='editar_produtos'),    
    path('editar/<int:id>/', views.editar, name='editar'),    
    path('visualizar/<int:id>/', views.visualizar, name="visualizar"),    
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)