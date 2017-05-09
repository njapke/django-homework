from django.conf.urls import url

from . import views

app_name = 'todolist' #namespace für <li><a href="{% url 'todolist:edit' todo.id %}">{{ question.question_text }}</a></li> in template

urlpatterns = [
    url(r'^$', views.index, name='index'), #/todolist/
    url(r'^sitenotice', views.sitenotice, name='sitenotice'),
    url(r'^howto', views.how_to, name='how_to'),
    url(r'^(?P<todo_id>[0-9]+)/$', views.edit, name='edit'),
    url(r'^create',views.create,name='create'),
]
