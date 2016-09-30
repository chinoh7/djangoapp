from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Postear

def post_list(request):
	posts = Postear.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
	return render(request, 'blog/listar_articulos.html',{'posts': posts})

def post_detail(request, pk):
        post = get_object_or_404(Postear, pk=pk)
        return render(request, 'blog/detalle_articulo.html', {'Postear': post})
