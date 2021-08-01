from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required
from django.conf import settings 

# Create your views here.
@login_required(login_url='login')
def createPost(request):
    form = CreatePostForm()
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.profile = Profile.objects.get(user=request.user)
            post.save()
            return redirect('profile')

    context = {'form':form}
    return render(request, 'posts/create_post.html', context)


@login_required(login_url='login')
def updatePost(request, pk):
    post = Post.objects.get(id=pk)
    form = UpdatePostForm(instance=post)
    if request.method == 'POST':
        form = UpdatePostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()

    context={'form':form, 'post':post, 'media_url':settings.MEDIA_URL}
    return render(request, 'posts/update_post.html', context)


@login_required(login_url='login')
def deletePost(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == "POST":
        post.delete()
        return redirect('profile')

    context = {'item':post}
    return render(request, 'posts/delete_post.html', context)