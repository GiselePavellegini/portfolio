from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm, ContatoForm

def lista_posts(request):
    busca = request.GET.get('q')
    if busca:
        posts = Post.objects.filter(titulo__icontains=busca).order_by('-data_publicacao')
    else:
        posts = Post.objects.all().order_by('-data_publicacao')
    return render(request, 'portfolio/lista_posts.html', {'posts': posts, 'busca': busca})

def criar_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_posts')
    else:
        form = PostForm()
    return render(request, 'portfolio/criar_post.html', {'form': form})

def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contato_sucesso')
    else:
        form = ContatoForm()
    return render(request, 'portfolio/contato.html', {'form': form})

def contato_sucesso(request):
    return render(request, 'portfolio/contato_sucesso.html')

# Aqui adiciona a view home que está faltando
def home(request):
    return render(request, 'portfolio/home.html')


