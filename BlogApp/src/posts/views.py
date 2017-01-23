from urllib import quote_plus
from django.db.models import Q
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

from .models import Post
from .forms import PostForm

def listView(request):
	queryset = Post.objects.all()
	qs = request.GET.get("q")
	if qs:
		queryset = queryset.filter(
				Q(title__icontains=qs) |
				Q(content__icontains=qs) 
			).distinct()

	paginator = Paginator(queryset, 5)
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)	

	context = {
		"posts": queryset,
		"page_request_var": page_request_var
	}
	return render(request, "list_view.html", context)

def detailView(request, year, month, day, slug):
	#instance = Post.objects.get(id=id)
	instance = get_object_or_404(Post, slug=slug,
									   timestamp__year=year,
									   timestamp__month=month,
									   timestamp__day=day)
	share_string = quote_plus(instance.content)
	context = {
		"post": instance,
		"share_string": share_string,
	}	
	return render(request, "detail_view.html", context)

def createView(request):
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		messages.success(request, "Successfully Created")
		return redirect(instance.get_absolute_url())
	context = {
		"title": "Post",
		"verb": "Create",
		"form": form,
	}
	return render(request, "post_form.html", context)

def updateView(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	# try:
	# 	instance = Post.objects.get(id=id)
	# except:
	# 	raise Http404	
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Successfully Updated")
		return redirect(instance.get_absolute_url())
	context = {
		"title": instance.title,
		"form": form,
		"verb": "Update",
	}
	return render(request, "post_form.html", context)	


def deleteView(request, slug=None):
	#instance = Post.objects.get(id=id)
	instance = get_object_or_404(Post, slug=slug)
	if request.method == "POST":
		instance.delete()
		messages.success(request, "Successfully Deleted")
		return redirect("posts:list")
	context = {
		"post": instance,
	}	
	return render(request, "confirm_delete.html", context)


				

