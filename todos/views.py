from django.shortcuts import render
from .models import Todo

# Create your views here.
def new(request):
    return render(request, 'new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    due_date = request.GET.get('due-date')
    
    # todo = Todo()
    # todo.title = todo
    # todo.content = content
    # todo.due_date = due_date
    # todo.save()

    todo = Todo(title=title, content=content, due_date=due_date)
    todo.save()
    return render(request, 'create.html')

def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos,
    }
    return render(request, 'index.html', context)

def detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    context = {
        'todo': todo,
    }
    return render(request, 'detail.html', context)

def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()

    return render(request, 'delete.html')

def edit(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo_date = todo.due_date.strftime('%Y-%m-%d')
    context = {
        'todo': todo,
        'todo_date': todo_date,
    }
    return render(request, 'edit.html', context)

def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.title = request.GET.get('title')
    todo.content = request.GET.get('content')
    todo.due_date = request.GET.get('due-date')
    todo.save()
    return render(request, 'update.html')