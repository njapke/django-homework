from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from todolist.models import Todo #import nicht vergessen
from django.template import loader
from django.http import Http404
from .forms import TodoForm, DeleteForm
from django import urls

def index(request):
    if request.method == "POST":
        form = DeleteForm(request.POST)
        if form.is_valid():
            delete_id = form.cleaned_data['delete']
            if Todo.objects.filter(pk=delete_id):
                todel = Todo.objects.get(pk=delete_id)
                todel.delete()
            
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


def create(request):
    if request.method == "POST":
        #compute data and either send to index or return error. maybe do this in index?
        form = TodoForm(request.POST)
        if form.is_valid():
            taskd = form.cleaned_data['task']
            dued = form.cleaned_data['date']
            completiond = form.cleaned_data['completion']
            
            newTodo= Todo(task= taskd, due_date= dued, completion=completiond)
            newTodo.save()

            return HttpResponseRedirect(urls.reverse('todolist:index'))
        
    
    template = loader.get_template('todolist/create.html')
    form= TodoForm()    #neue todoform wird zur eingabe erstellt
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))

def sitenotice(request):
    return render(request, 'todolist/sitenotice.html')
    