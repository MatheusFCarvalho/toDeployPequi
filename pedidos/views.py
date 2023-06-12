from django.shortcuts import render, redirect
from .models import Pedido
from .forms import PedidoForm
from my_user.models import User
from django.views.decorators.csrf import csrf_protect

    
@csrf_protect
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']
        
        # Verifique o valor de 'role' para determinar a cor do fundo e o título
        if role == 'produtor':
            background_color = '#ff0000'  # Cor do fundo para o produtor
            title = 'Entrando como produtor'
        elif role == 'vendedor':
            background_color = '#00ff00'  # Cor do fundo para o vendedor
            title = 'Entrando como vendedor'
        
        # Redirecione para a seção especificada (produtor ou vendedor)
        if role == 'produtor':
            return redirect('produtor')
        elif role == 'vendedor':
            return redirect('vendedor')

    return render(request, 'login.html')

def produtor(request):

    if request.method == 'POST':
        form = PedidoForm(request.POST)
        
        user = User.objects.filter(username='produção')[0]

        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.created_by = user
            pedido.updated_by = user
            pedido.save()
            return redirect('produtor')

    else:
        form = PedidoForm()

    pedidos = Pedido.objects.all().order_by('-updated_at')
    return render(request, 'produtor.html', {'pedidos': pedidos, 'form': form})

def vendedor(request):
    pedidos = Pedido.objects.all().order_by('-updated_at')
    return render(request, 'vendedor.html', {'pedidos': pedidos})

def resetPedidos(request):
    pedidos, form = getPedidoForm()
    Pedido.objects.all().delete()
    return redirect('pedidos:home')

def getPedidoForm():
    pedidos = Pedido.objects.all().order_by('-updated_at')
    form = PedidoForm()
    return {pedidos, form}