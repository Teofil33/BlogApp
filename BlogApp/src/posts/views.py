from django.shortcuts import render, redirect

# Create your views here.

from .models import Post
from .forms import PostForm

def listView(request):
	queryset = Post.objects.all()
	context = {
		"posts": queryset,
	}
	return render(request, "list_view.html", context)

def detailView(request, id):
	queryset = Post.objects.get(id=id)
	context = {
		"post": queryset,
	}	
	return render(request, "detail_view.html", context)

def createView(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return redirect(instance.get_absolute_url())
	context = {
		"form": form,
	}
	return render(request, "post_form.html", context)		

