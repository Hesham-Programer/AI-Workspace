from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoList
from auth.forms import CreateUserForm
# Create your views here.
print(CreateUserForm.Meta.model())
@login_required(login_url="my-login")
def index_todolist(request):
    if request.method == "POST":

        if "add" in request.POST:
            print("add")

            todo = request.POST.get("todo")
            TodoList.objects.create(todo=todo)

            for item in TodoList.objects.all():
                print(item.todo)

            return redirect("home_page")

        if "delete" in request.POST:
            note_id = request.POST.get("delete")
            print(note_id)
            todo = get_object_or_404(TodoList, id=note_id)
            todo.delete()

    context = {
        "todos": TodoList.objects.all()
    }

    return render(request, template_name="todolist/index.html", context=context)

@login_required(login_url="my-login")
def edit_todo(request, todo_id):
    context = {
        "todo_id": todo_id,
    }
    if "done" in request.POST:
        print("done")
        new_todo = request.POST.get("new_todo")

        todos = get_object_or_404(TodoList, id=todo_id)
        todos.todo = new_todo

        todos.save()

        return redirect("home_page")
    return render(request, template_name="todolist/edit.html", context=context)
