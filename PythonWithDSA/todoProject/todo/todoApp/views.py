from django.shortcuts import render, redirect
from .models import ToDoModel
# Create your views here.

def addTask(request):
    if request.method=='POST':
        title = request.POST.get('title')
        priority = request.POST.get('priority')
        notes = request.POST.get('notes')
        status = request.POST.get('status')
        dueDate = request.POST.get('dueDate')

        ToDoModel.objects.create(
            title=title,
            priority = priority,
            notes=notes,
            status=status,
            duedate=dueDate
        )
        return redirect('main')
    todos = ToDoModel.objects.all()
    return render(request,'index.html', {'todos':todos})

def updateStatus(request,id):
    todo = ToDoModel.objects.get(id=id)
    status = todo.status
    if status=='P':
        todo.status = 'C'
    else:
        todo.status = 'P'
    
    todo.save()
    return redirect('main')

def delete(request,id):
    todo = ToDoModel.objects.get(id=id)
    todo.delete()
    return redirect('main')
