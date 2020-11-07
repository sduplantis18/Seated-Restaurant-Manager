from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic, Entry, Menu
from .forms import MenuForm, TopicForm, EntryForm

# Create your views here.
def index(request):
    """The home page for learning_logs"""
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """Show all topics"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics':topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """Show a single topic and all its entries"""
    # query db for topic id and store in topic variable
    topic = Topic.objects.get(id=topic_id)
    # Make sure the topic belongs to the current user
    if topic.owner != request.user:
        raise Http404

    # query db for entries for each topic and sort by date added. The minus sign in front of date_added sorts in reverse order.
    entries = topic.entry_set.order_by('-date_added')
    # store the topic and the entries in a dictionary
    context = {'topic': topic, 'entries': entries}
    # send the context to the template
    return render(request, 'learning_logs/topic.html', context)


@login_required
def entries(request, topic_id):
    """Show list of all entries within a topic"""
    entries = Entry.objects.filter(id=topic_id)
    context = {'entries':entries}
    return render(request, 'learning_logs/entries.html', context)


@login_required
def entry(request, entry_id):
    """Show a single entry (menu) & all its menu items"""
    # query DB for entry id and store in entry variable
    entry = Entry.objects.get(id=entry_id)
    # Make sure the entry belongs to the current user
    """
    if entry.owner != request.user:
        raise Http404
    """
    # query db for each menu in an entry (restaurant)
    menus = entry.menu_set.order_by('title')
    # store the menu and menu items in a dictionary
    context = {'entry':entry, 'menus':menus}

    # send the context to the template
    return render(request, 'learning_logs/entry.html', context) 

@login_required
def new_topic(request):
    """Add a new topic"""
    if request.method != 'POST':
        # No date submitted; create a blank form
        form = TopicForm()
    else:
        # Post data submitted: process data
        form = TopicForm(request.POST, request.FILES)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')
    # Display a blank or invalid form
    context = {'form':form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Add new restaurant associated within a venue"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # No data submitted; then create a blank form
        form = EntryForm()
    else:
        # POST data submitted; process data
        form = EntryForm(request.POST, request.FILES)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
    
    # Display a blank or invalid form.
    context = {'topic':topic, 'form':form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        # Initial request; pre-fill form with current entry
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid:
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry':entry, 'topic':topic, 'form':form}
    return render(request, 'learning_logs/edit_entry.html', context)


@login_required
def delete_topic(request, topic_id):
    """Delete a Topic"""
    topic = Topic.objects.get(id=topic_id)

    if request.method == 'POST':
        topic.delete()
        return redirect('learning_logs:topics')

    context = {'topic':topic}
    return render(request, 'learning_logs/delete_topic.html', context)


@login_required
def new_menu(request, entry_id):
    """Add a new menu to a restaurant"""
    entry = Entry.objects.get(id=entry_id)
    # Intial load of the form
    if request.method != 'POST':
        form = MenuForm()
    # Post and process the data
    else:
        form = MenuForm(request.POST)
        if form.is_valid:
            new_menu = form.save(commit=False)
            new_menu.entry = entry
            form.save()
            return redirect('learning_logs:entry', entry_id=entry_id)
    
    # display context and render the html to display the form
    context = {'entry':entry, 'form':form }
    return render(request, 'learning_logs/new_menu.html', context)


@login_required
def menu(request, menu_id):
    """View a menu & its menu_items"""
    # query db for specific menu_id and store in menu variable
    menu = Menu.objects.get(id=menu_id)
    # Make sure the topic belongs to the current user
    """
    if menu.owner != request.user:
        raise Http404
    """
    # query db for menu_items for each menu and sort by title 
    menu_items = menu.menu_item_set.order_by('title')
    # store the menu and the menu items in a dictionary
    context = {'menu': menu, 'menu_items': menu_items}
    # send the context to the template
    return render(request, 'learning_logs/menu.html', context)