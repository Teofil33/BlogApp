from urllib import quote_plus
from django.db.models import Q
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

from comments.forms import CommentForm
from comments.models import Comment
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
	instance = get_object_or_404(Post, slug=slug,
									   timestamp__year=year,
									   timestamp__month=month,
									   timestamp__day=day)
	share_string = quote_plus(instance.content)
	comments = Comment.objects.filter(post=instance)
	form = CommentForm(request.POST or None)
	if form.is_valid():
		parent_id = request.POST.get('parent_id')
		parent_comment = None
		if parent_id:
			parent_comment = Comment.objects.get(id=parent_id)
		new_instance = form.save(commit=False)
		if parent_comment:
			new_instance.parent = parent_comment
		new_instance.user = request.user
		new_instance.post = instance
		#new_instance.content = comment_form.cleaned_data.get("content")
		new_instance.save()
		return redirect(instance.get_absolute_url())	
	context = {
		"post": instance,
		"share_string": share_string,
		"comments": comments,
		"comment_form": form,
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

#def updateView(request, year, month, day, slug=None):
def updateView(request, slug):
	instance = get_object_or_404(Post, slug=slug)
	# instance = get_object_or_404(Post, slug=slug,
	# 							   timestamp__year=year,
	# 							   timestamp__month=month,
	# 							   timestamp__day=day)	
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

# Trying to make deleteView, so it can have date in it's url
#def deleteView(request, year, month, day, slug=None):
	# instance = get_object_or_404(Post, slug=slug,
	# 							   timestamp__year=year,
	# 							   timestamp__month=month,
	# 							   timestamp__day=day)

	# if request.method == "POST":
	# 	instance.delete()
	# 	messages.success(request, "Successfully Deleted")
	# 	return redirect("posts:list")

	# year = instance.timestamp.year
	# month = instance.timestamp.year
	# day = instance.timestamp.year

	# 	context = {
	# 	"year": year,
	# 	"month": month,
	# 	"day": day,
	# 	"post": instance,
	# }

	#return render(request, "confirm_delete.html", context)

def deleteView(request, slug):
	instance = get_object_or_404(Post, slug=slug)	
	if request.method == "POST":
		instance.delete()
		messages.success(request, "Successfully Deleted")
		return redirect("posts:list")
	context = {
		"post": instance,
	}	
	return render(request, "confirm_delete.html", context)


				

