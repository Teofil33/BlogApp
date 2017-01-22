from django.shortcuts import render

# Create your views here.

from .models import Post

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

