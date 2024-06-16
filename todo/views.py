from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone 
from todo.models import Item

def TodoAppView(request):
    all_items = Item.objects.all()
    return render(request, 'todolist.html', {'all_items': all_items, 'ACTION_URL': '/todo/'})

def AddTodo(request):
    if request.method == 'POST' and request.POST['content'].strip() != '':
        new_item = Item(content=request.POST['content'])
        new_item.save()
    return HttpResponseRedirect('/')

# Delete Todo
def DeleteTodo(request, item_id):
    item_to_delete = get_object_or_404(Item, id=item_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/')

# Edit Todo
def EditTodo(request, item_id):
    all_items = Item.objects.all()
    item_to_edit = get_object_or_404(Item, id=item_id)
    return render(request, 'todolist.html', {'edit_item': item_to_edit, 'all_items': all_items})

# Update Todo Item
def UpdateTodoItem(request, item_id):
    if request.method == 'POST':
        item_to_update = get_object_or_404(Item, id=item_id)
        item_to_update.content = request.POST['content']
        # Update the created_time field to the current time
        item_to_update.created_time = timezone.now()
        item_to_update.save()
    return HttpResponseRedirect('/')
