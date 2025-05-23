from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from django.contrib import messages
from .forms import TodoForm
from .models import Todo


def todos(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('todos')
    else:
        form = TodoForm()
    todos = Todo.objects.all()

    return render(request, 'todos.html' , {'todos': todos, 'form':form})

def todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)

    return render(request, 'todo.html',{'todo':todo})

# in views.py
def delete_todo(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('todos')

def login_view(request):
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print("POST:", request.POST)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('todos')
        
        else:
            error = 'Invalid username or password '

    return render(request, 'login.html', {'error': error})


def todo_view(request):
    return render(request, 'todos.html')
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # automatically login after signup
            return redirect('todos')  # redirect to your todos page
        else:
            # form invalid (e.g. username taken), errors handled by form
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

