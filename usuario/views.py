from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import check_password
from .models import Produto
from .models import Usuario
from django.db.models import Q
# Create your views here.

def verificar_session(request):
    if request.session.get('id', False):
        return
    else:
        return render(request, 'usuario/usuario_login.html')
def home_usuario(request):
    # resultado = verificar_session(request)
    # if resultado:
    #     return resultado
    produtos = Produto.objects.filter(apagado=False)
    if request.method=="POST":
        categoria = request.POST.get('categoria')
        buscar = request.POST.get('buscar')
        if buscar and categoria:
            produtos = Produto.objects.filter(Q(nome__startswith=buscar), categoria=categoria, apagado=False)
            context = {
                'escrita': produtos.filter(categoria="ESCRITA"),
                'papeis': produtos.filter(categoria="PAPEIS"),
                'org': produtos.filter(categoria="ORG"),
                'artes': produtos.filter(categoria="ARTES"),
                'escolar': produtos.filter(categoria="ESCOLAR"),
            }
            return render(request, 'usuario/usuario_home.html', context)
        if buscar:
            produtos = Produto.objects.filter(Q(nome__startswith=buscar), apagado=False)
            context = {
                'escrita': produtos.filter(categoria="ESCRITA"),
                'papeis': produtos.filter(categoria="PAPEIS"),
                'org': produtos.filter(categoria="ORG"),
                'artes': produtos.filter(categoria="ARTES"),
                'escolar': produtos.filter(categoria="ESCOLAR"),
            }
            return render(request, 'usuario/usuario_home.html', context)
        if categoria:
            produtos = Produto.objects.filter(categoria=categoria, apagado=False)
            context = {
                'escrita': produtos.filter(categoria="ESCRITA"),
                'papeis': produtos.filter(categoria="PAPEIS"),
                'org': produtos.filter(categoria="ORG"),
                'artes': produtos.filter(categoria="ARTES"),
                'escolar': produtos.filter(categoria="ESCOLAR"),
            }
            return render(request, 'usuario/usuario_home.html', context)
        context = {
            'escrita': produtos.filter(categoria="ESCRITA"),
            'papeis': produtos.filter(categoria="PAPEIS"),
            'org': produtos.filter(categoria="ORG"),
            'artes': produtos.filter(categoria="ARTES"),
            'escolar': produtos.filter(categoria="ESCOLAR"),
        }
        return render(request, 'usuario/usuario_home.html', context)
    else:
        context = {
            'escrita': produtos.filter(categoria="ESCRITA"),
            'papeis': produtos.filter(categoria="PAPEIS"),
            'org': produtos.filter(categoria="ORG"),
            'artes': produtos.filter(categoria="ARTES"),
            'escolar': produtos.filter(categoria="ESCOLAR"),
        }
        return render(request, 'usuario/usuario_home.html', context)
def visualizar(request, id):
    produto = get_object_or_404(Produto, id=id)
    return render(request, "usuario/usuario_visualizar.html", {'produto': produto})
def login(request):
    return render(request, "usuario/usuario_login.html")
def login_tratar(request):
    if request.method=="POST":
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        try:
            usuario = Usuario.objects.get(email=email)  # busca pelo email
        except Usuario.DoesNotExist:
            return redirect('usuario:login')
        if check_password(senha, usuario.senha):
            request.session.set_expiry(0)
            request.session['id'] = usuario.id
            return redirect('usuario:home')
        else:
            return redirect('usuario:login')
        
def sign_usuario(request):
    ...
def sign():
    ...