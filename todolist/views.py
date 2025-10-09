from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoList
import markdown

# Create your views here.
def index(request):
    if request.method == "POST":

        if "add" in request.POST:
            print("add")

            todo = request.POST.get("todo")
            TodoList.objects.create(todo=todo)

            for item in TodoList.objects.all():
                print(item.todo)

            redirect("home_page")

        if "delete" in request.POST:
            note_id = request.POST.get("delete")
            todo = get_object_or_404(TodoList, id=note_id)
            todo.delete()

    context = {
        "todos": TodoList.objects.all()
    }

    return render(request, template_name="todolist/index.html", context=context)


def edit(request, todo_id):
    context = {
        "todo_id": todo_id,
    }
    return render(request, template_name="todolist/edit.html", context=context)
