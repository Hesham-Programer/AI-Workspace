from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoList


# Create your views here.


@login_required(login_url="my-login")
def index_todolist(request):
    if request.method == "POST":

        if "add" in request.POST:
            print("add")

            todo = request.POST.get("todo")
            if todo is not "":
                TodoList.objects.create(todo=todo)

            return redirect("home_page")

        if "delete" in request.POST:
            note_id = request.POST.get("delete")
            print(note_id)
            todo = get_object_or_404(TodoList, id=note_id)
            todo.delete()

        if "complete" in request.POST:
            note_id = request.POST.get("complete")
            todo = get_object_or_404(TodoList, id=note_id)

            if not todo.completed:
                todo.completed = True
            else:
                todo.completed = False
            todo.save()

            print(todo)
            return redirect("home_page")

    context = {
        "todos": TodoList.objects.all(),
    }

    return render(request, template_name="todolist/index.html", context=context)


@login_required(login_url="my-login")
def edit_todo(request, todo_id):
    if "done" in request.POST:
        new_todo = request.POST.get("new_todo")

        todos = get_object_or_404(TodoList, id=todo_id)
        todos.todo = new_todo
        todos.save()

        return redirect("home_page")
    context = {
        "todo_id": todo_id,
    }
    return render(request, template_name="todolist/edit.html", context=context)


@login_required(login_url="my-login")
def completed_todos(request):
    return render(request, template_name="todolist/completed_todos.html", context={
        "todos": TodoList.objects.filter(completed=True),
    }
    )
