from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import check_password
from .models import Produto
from .models import Dona
from django.db.models import Q
# from PIL import Image

def verificar_session(request):
    if request.session.get('dona', False):
        return
    else:
        return render(request, 'produtos/produtos_login.html')
def login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    try:
        dona = Dona.objects.get(email=email)  # busca pelo email
    except Dona.DoesNotExist:
        return redirect('produtos:login')
    if check_password(senha, dona.senha):
            request.session.set_expiry(0)
            request.session['dona'] = True
            return redirect('produtos:home')
    else:
            return redirect('produtos:login')
# Create your views here.
def home_produtos(request):
    resultado = verificar_session(request)
    if resultado:  # Se a sessão não existe, resultado será o render do login
        return resultado
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
            return render(request, 'produtos/produtos_home.html', context)
        if buscar:
            produtos = Produto.objects.filter(Q(nome__startswith=buscar), apagado=False)
            context = {
                'escrita': produtos.filter(categoria="ESCRITA"),
                'papeis': produtos.filter(categoria="PAPEIS"),
                'org': produtos.filter(categoria="ORG"),
                'artes': produtos.filter(categoria="ARTES"),
                'escolar': produtos.filter(categoria="ESCOLAR"),
            }
            return render(request, 'produtos/produtos_home.html', context)
        if categoria:
            produtos = Produto.objects.filter(categoria=categoria, apagado=False)
            context = {
                'escrita': produtos.filter(categoria="ESCRITA"),
                'papeis': produtos.filter(categoria="PAPEIS"),
                'org': produtos.filter(categoria="ORG"),
                'artes': produtos.filter(categoria="ARTES"),
                'escolar': produtos.filter(categoria="ESCOLAR"),
            }
            return render(request, 'produtos/produtos_home.html', context)
        context = {
            'escrita': produtos.filter(categoria="ESCRITA"),
            'papeis': produtos.filter(categoria="PAPEIS"),
            'org': produtos.filter(categoria="ORG"),
            'artes': produtos.filter(categoria="ARTES"),
            'escolar': produtos.filter(categoria="ESCOLAR"),
        }
        return render(request, 'produtos/produtos_home.html', context)
    else:
        context = {
            'escrita': produtos.filter(categoria="ESCRITA"),
            'papeis': produtos.filter(categoria="PAPEIS"),
            'org': produtos.filter(categoria="ORG"),
            'artes': produtos.filter(categoria="ARTES"),
            'escolar': produtos.filter(categoria="ESCOLAR"),
        }
        return render(request, 'produtos/produtos_home.html', context)
def ver_produtos(request):
    resultado = verificar_session(request)
    if resultado:  # Se a sessão não existe, resultado será o render do login
        return resultado
    produtos = Produto.objects.filter(apagado=False)
    
    context = {
        'escrita': produtos.filter(categoria="ESCRITA"),
        'papeis': produtos.filter(categoria="PAPEIS"),
        'org': produtos.filter(categoria="ORG"),
        'artes': produtos.filter(categoria="ARTES"),
        'escolar': produtos.filter(categoria="ESCOLAR"),
    }
    return render(request, 'produtos/produtos_ver.html', context)
def criar_produtos(request):
    resultado = verificar_session(request)
    if resultado:  # Se a sessão não existe, resultado será o render do login
        return resultado
    return render(request, 'produtos/produtos_criar.html')
def criar(request):
    resultado = verificar_session(request)
    if resultado:  # Se a sessão não existe, resultado será o render do login
        return resultado
    if request.method=="POST":
        nome = request.POST.get('nome')
        marca = request.POST.get('marca')
        descricao = request.POST.get('descricao')
        preco = str(request.POST.get('preco')).replace(",", ".")
        img = request.FILES.get("img")
        categoria = request.POST.get('categoria')
        if nome is not None and descricao is not None and preco is not None and img is not None and categoria:
            produto = Produto(nome=nome, marca=marca, descricao=descricao, preco=preco, img=img, categoria=categoria)
            produto.save()
            return redirect('produtos:ver_produtos')
        else:
            return redirect('produtos:criar_produtos')
    return redirect('produtos:criar_produtos')
# def deletar(request, id):
#     if request.method=="POST":
#         produto  = get_object_or_404(Produto, id=id)
#         produto.delete()
#         return redirect("produtos:ver_produtos")
#     return redirect("produtos:ver_produtos")
def editar_produtos(request, id):
    resultado = verificar_session(request)
    if resultado:  # Se a sessão não existe, resultado será o render do login
        return resultado
    if request.method=="POST":
        produto  = get_object_or_404(Produto, id=id)
        return render(request, "produtos/produtos_editar.html", {'produto':produto})
    return render(request, "produtos/produtos_ver.html")
def editar(request, id):
    resultado = verificar_session(request)
    if resultado:  # Se a sessão não existe, resultado será o render do login
        return resultado
    if request.method=="POST":
        produto  = get_object_or_404(Produto, id=id)
        novo_nome = request.POST.get("nome")
        novo_preco = str(request.POST.get("preco")).replace(",", ".")
        nova_marca = request.POST.get("marca")
        nova_descricao = request.POST.get("descricao")
        nova_img = request.FILES.get("img")
        nova_categoria = request.POST.get('categoria')
        if novo_nome:
            produto.nome = novo_nome
        if novo_preco:
            produto.preco = novo_preco
        if nova_marca:
            produto.marca = nova_marca
        if nova_descricao:
            produto.descricao = nova_descricao
        if nova_img:
            produto.img = nova_img
        if nova_categoria:
            produto.categoria = nova_categoria
        produto.save()
        return redirect("produtos:ver_produtos")
    return redirect("produtos:ver_produtos")
def deletar(request, id):
    resultado = verificar_session(request)
    if resultado:  # Se a sessão não existe, resultado será o render do login
        return resultado
    if request.method=="POST":
        produto  = get_object_or_404(Produto, id=id)
        produto.apagado = True
        produto.save()
        return redirect("produtos:ver_produtos")
    return redirect("produtos:ver_produtos")
def visualizar(request, id):
    resultado = verificar_session(request)
    if resultado:  # Se a sessão não existe, resultado será o render do login
        return resultado
    produto = get_object_or_404(Produto, id=id)
    return render(request, "produtos/produtos_visualizar.html", {'produto': produto})
