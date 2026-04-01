from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'usuario' 

urlpatterns=[
    path('', views.home_usuario, name='home'),
    path('visualizar/<int:id>/', views.visualizar, name="visualizar"),
    path('login_tratar/', views.home_usuario, name="login_tratar"),
    path('login/', views.login, name="login"),

]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)