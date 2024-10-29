from django.shortcuts import render, redirect
from .import forms
from .import models
from .models import Post
from .forms import PostForm,SearchForm
def add_post(request):
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('add_post')
        
    else:
        post_form = forms.PostForm()
        
    return render(request, 'add_post.html',{'form': post_form})


def edit_post(request, id):
    post = models.Post.objects.get(pk=id)
    post_form = forms.PostForm(instance=post)
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('add_post')
        
    else:
        post_form = forms.PostForm()
        
    return render(request, 'add_post.html',{'form': post_form})

def delete_post(request, id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    
    return redirect ('homepage')


def search(request):
    events = Post.objects.all()
    search_form = SearchForm(request.POST)
    search_term = ""
    if search_form.is_valid():
        search_term = search_form.cleaned_data["query"]
    searched_event = []
    for event in events:
        if search_term and search_term in event.title.lower():
            searched_event.append(event)
    context = {
        "events":searched_event,
        "search_form":search_form,
    }
    return render(request,"search_results.html",context=context)
