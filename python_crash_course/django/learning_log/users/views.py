from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm


def logout_view(request):
    """Fazendo logout"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request):
    """Registrando um novo usuario"""
    if request.method != 'POST':
        # Mostrar formulario em branco
        form = UserCreationForm()
    else:
        # Processar os dados do novo usuario
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Fazer login do novo usuario
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))
    context = {'form': form}
    return render(request, 'users/register.html', context)
