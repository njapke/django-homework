from django.shortcuts import render
from django.http import HttpResponse
from todolist.models import Todo #import nicht vergessen
from django.template import loader
from django.http import Http404


def index(request):
    todos = Todo.objects.all()
    template = loader.get_template('todolist/index.html')
    context = {
        'todos': todos,
    }
    return HttpResponse(template.render(context, request))  # kürzer möglich, aber vorerst so. kürzer: https://docs.djangoproject.com/en/1.10/intro/tutorial03/

def edit(request, todo_id):
    try:                                        #geht auch ohne try mit  todo = get_object_or_404(Todo, pk=todo_id)   (Model,argumente..)
        todo = Todo.objects.get(pk=todo_id)
    except Todo.DoesNotExist:
        raise Http404("Todo does not exist")
    return render(request, 'todolist/edit.html', {'todo':todo}) # hier kürzer render(request,view,context-dictionary)
# Create your views here.
