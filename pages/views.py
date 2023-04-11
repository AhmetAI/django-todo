from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User


from pages.models import Todo

# Create your views here.
@login_required
def index(request):
    
    todos = Todo.objects.filter(author=request.user)
    firstTodo = todos.first()
    if not firstTodo:
        return render(request, "pages/index.html", {"error":"You haven't created any todos yet."})
    
    return render(request, "pages/index.html", {"todos":todos, "firstTodo":firstTodo})



@login_required
def details(request, slug):
    mytodos = get_object_or_404(Todo, slug=slug, author=request.user)
    todos = Todo.objects.filter(author=request.user)
    
    return render(request, "pages/todo.html", {"mytodo":mytodos, "slug":slug, "todos":todos})

@login_required
def delete(request, id):
    todo = get_object_or_404(Todo, pk=id)
    if request.method == "POST":
        todo.delete()
        return redirect("index")
    else:
        return redirect("index")

@login_required
def edit(request, id):
    todo = get_object_or_404(Todo, pk=id)
    if request.method == "POST":
        todo.title = request.POST["newTitle"]
        todo.description = request.POST["newDescription"]
        todo.save()

       
        return redirect("index")
    else:
        return redirect("index")
        
@login_required
def create(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        newTodo = Todo(title=title, description=description, author=request.user)
        newTodo.save()
        return redirect("index")
        


