from django.shortcuts import render, redirect, get_object_or_404

from .forms import NewPostForm
from django.contrib.auth.decorators import login_required

from .models import Post, Tag, Stream, Likes, PostFileContent
from authy.models import Profile

from stories.models import Story, StoryStream
from comment.models import Comment
from comment.forms import CommentForm

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


@login_required
def index(request, *args, **kwargs):
	user = request.user
	posts = Stream.objects.filter(user=user)

	stories = StoryStream.objects.filter(user=user)

	group_ids = []

	for post in posts:
		
		group_ids.append(post.post_id)

	
	post_items = Post.objects.filter(id__in=group_ids).all().order_by('-posted')


	y = []
	for x in post_items:

		if Likes.objects.filter(post=x.id ,user=user).exists():
			x.liked = True
		else:
			x.liked = False

		y.append(x)

		
	context = {
		'post_items':y,
		'stories':stories,

		}


	return render(request, 'posts/index.html', context)


@login_required
def newpost(request):

	user = request.user
	tags_objs = []
	files_objs = []

	if request.method == 'POST':
		form = NewPostForm(request.POST, request.FILES)
		if form.is_valid():
			files = request.FILES.getlist('content')
			caption = form.cleaned_data.get('caption')
			tags_form = form.cleaned_data.get('tags')

			tags_list = list(tags_form.split(','))

			for tag in tags_list:
				t, created = Tag.objects.get_or_create(title=tag)
				tags_objs.append(t)

			for file in files:
				file_instance = PostFileContent(file=file, user=user)
				file_instance.save()
				files_objs.append(file_instance)

			p, created = Post.objects.get_or_create(caption=caption, user=user)
			p.tags.set(tags_objs)
			p.content.set(files_objs)
			p.save()
			return redirect('index')
	else:
		form = NewPostForm()

	context = {

		'form': form,

	}

	return render(request, 'posts/newpost.html', context)


def post_detail(request, post_id):
	posts = get_object_or_404(Post, id=post_id)
	user = request.user


	#comment
	comments = Comment.objects.filter(post=posts).order_by('date')

	#ajax
	form = CommentForm()

	#comment Form
	# if request.method == 'POST':
	# 	form = CommentForm(request.POST)
	# 	if form.is_valid():
	# 		comment = form.save(commit=False)
	# 		comment.post = posts
	# 		comment.user = user
	# 		comment.save()
	# 		return HttpResponseRedirect(reverse('postdetails', args=[post_id]))
	# else:
	# 	form = CommentForm()


	context = {
		'posts':posts,
		'comments': comments,
		'form':form,
	}

	return render(request, 'posts/post_detail.html', context)


def like(request, post_id):
	user = request.user
	post = Post.objects.get(id=post_id)
	current_likes = post.likes
	print(request.method)
	
	liked = Likes.objects.filter(user=user, post=post).count()

	if not liked:
		like = Likes.objects.create(user=user, post=post)
		#like.save()
		current_likes += 1

	else:
		Likes.objects.filter(user=user, post=post).delete()
		current_likes -= 1

	post.likes = current_likes
	post.save()

	return HttpResponseRedirect(reverse('index'))


@login_required
def favorite(request, post_id):
	user = request.user
	post = Post.objects.get(id=post_id)
	profile = Profile.objects.get(user=user)

	if profile.favorites.filter(id=post_id).exists():
		profile.favorites.remove(post)

	else:
		profile.favorites.add(post)

	return HttpResponseRedirect(reverse('index'))





def tags(request, tag_slug):
	tag = get_object_or_404(Tag, slug=tag_slug)
	posts = Post.objects.filter(tags=tag).order_by('-posted')

	context = {

		'posts': posts,
		'tag':tag
	}

	return render(request, 'tags/tag.html', context)

