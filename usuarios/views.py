from django.shortcuts import render, redirect

from usuarios.forms import LoginForms, CadastroForms

def login(request):
    form = LoginForms()
    return render(request, 'usuarios/login.html', {"form": form})

def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)
        # Valida se as senhas são iguais:
        if form["senha_1"].value() != form["senha_2"].value():
            return redirect('cadastro')
        
        print(form)
        
    
    return render(request, 'usuarios/cadastro.html', {"form": form})
