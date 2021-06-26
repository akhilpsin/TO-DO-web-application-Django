from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . models import Task
from . forms import TodoForm

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

#class based (just for learning purposes)
class Tasklistview(ListView):
    model=Task
    template_name='home.html'
    context_object_name='view_task'
class TaskDetailview(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'
class TaskUpdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields=('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('class_detail',kwargs={'pk':self.object.id})

class TaskDeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('class_home')

# class based ends here.......................    
# Create your views here.
def home(request):
    view_task = Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority = request.POST.get('priority','' )
        date = request.POST.get('date', '')
        task=Task(name=name,priority=priority,date=date)
        print('sucess')
        task.save()

    return render(request,'home.html',{'view_task':view_task})

def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,taskid):
    task=Task.objects.get(id=taskid)
    f=TodoForm(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task':task})
