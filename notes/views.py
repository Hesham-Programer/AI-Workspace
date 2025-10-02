from django.shortcuts import render, get_object_or_404, redirect
from .models import Notes


# Create your views here.

class Add:
    def __init__(self):
        pass

    def add(self, title: str, content: str):
        Notes.objects.create(title=title, content=content)

    def remove(self, note_id: int):
        note = get_object_or_404(Notes, id=note_id)
        note.delete()

    def edit(self, note_id: int, new_title: str, new_content: str):
        note = get_object_or_404(Notes, id=note_id)
        note.title = new_title
        note.content = new_content


def index(request):
    if request.method == "POST":
        if "add" in request.POST:
            note_title = request.POST.get("title")
            note_content = request.POST.get("content")

            Notes.objects.create(title=note_title, content=note_content)

            for note in Notes.objects.all():
                print(note.title, note.content)

            redirect("index")
        if "delete" in request.POST:
            note_id = request.POST.get("delete")
            note = get_object_or_404(Notes, id=note_id)
            note.delete()

            redirect("index")

    context = {
        "notes": Notes.objects.all()
    }
    return render(request, template_name="notes/index.html", context=context)

def edit(request, note_id):
    note = get_object_or_404(Notes, id=note_id)

    context = {
        "note_title":note.title,
        "note_content":note.content,
    }
    if request.method == "POST":

        if "save" in request.POST:
            new_title = request.POST.get("title")
            new_content = request.POST.get("content")

            notes = get_object_or_404(Notes, id=note_id)
            notes.title = new_title
            notes.content = new_content

            notes.save()

            return redirect("index")

    return render(request, "notes/edit.html", context=context)
