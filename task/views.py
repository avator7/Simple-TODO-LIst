from email import message
from urllib import response
from django.shortcuts import render,redirect
from . models import List
from django.contrib import messages
from .forms import ListForm
# Create your views here.

def home(request):
    all_items = List.objects.all
    if request.method == 'POST':
        form = ListForm(request.POST or None)


        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request,'task added')
            return render(request, 'register.html', {'all_items':all_items})

    else:
        all_items = List.objects.all
    return render(request, 'register.html', {'all_items':all_items})



def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.warning(request, "item deleted")
    return redirect('home')

def cross_off(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('home')

def uncross(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('home')


def edit(request, list_id):
    if request.method == 'POST':
        item = List.objects.get(pk=list_id)
        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, 'Item has been successfully edited.')
            return redirect('home')
    else: 
        item = List.objects.get(pk=list_id)
        return render(request, 'edit.html', {'item': item})