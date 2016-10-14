from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Postear
from .forms import PostearForm

def post_list(request):
	posts = Postear.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
	return render(request, 'blog/listar_articulos.html',{'posts': posts})

def post_detail(request, pk):
        post = get_object_or_404(Postear, pk=pk)
        return render(request, 'blog/detalle_articulo.html', {'Postear': post})

def post_new(request):
    if request.method == "POST":
        formulario = PostearForm(request.POST)
        if formulario.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.fecha_publicacion = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        formulario = PostearForm()
    return render(request, 'blog/post_edit.html', {'formulario': formulario})

def post_edit(request, pk):
    post = get_object_or_404(Postear, pk=pk)
    if request.method == "Postear":
        formulario = PostearForm(request.Postear, instance=Postear)
        if formulario.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('blog.views.detalle_articulo', pk=post.pk)
    else:
        formulario = PostearForm(instance=post)
    return render(request, 'blog/editar_articulo.html', {'formulario': formulario})
