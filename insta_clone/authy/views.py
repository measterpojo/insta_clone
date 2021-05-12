from django.shortcuts import render, get_object_or_404, redirect

from .models import Profile
from .forms import SignupForm, ChangePasswordForm, EditProfileForm, LoginForm
from django.contrib.auth.models import User
from posts.models import Post, Follow, Stream

from django.contrib.auth import update_session_auth_hash

from django.contrib.auth.decorators import login_required

from django.urls import resolve, reverse

from django.http import HttpResponse, HttpResponseRedirect


from django.db import transaction
from django.core.paginator import Paginator

from django.contrib.auth import authenticate, login

from django.contrib import messages

def login_request(request):
	if request.method == 'POST':
		form = LoginForm(request=request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}")
				return redirect('/')
			else:
				messages.error(request,"Invalid username or password." )
		else:
			messages.error(request,"Invalid username or password.")
	
	form = LoginForm()

	context = {

		'form':form
	}

	return render(request, 'authy/login.html', context)



def userprofile(request, username):
	user = get_object_or_404(User, username=username)
	profile = Profile.objects.get(user=user)
	url_name = resolve(request.path).url_name

	if url_name == 'profile':
		posts = Post.objects.filter(user=user).order_by('-posted')
	else:
		posts = profile.favorites.all()


	# posts_count = Post.objects.filter(user=user).count()
	# following_count = Follow.objects.filter(following=user).count()
	# followwers_count = Follow.objects.filter(following=user).count()


	follow_status= Follow.objects.filter(following=user, follower=request.user).exists()

	context = {

		'profile':profile,
		'posts':posts,
		'follow_status':follow_status

	}

	return render(request, 'authy/profile.html', context)

def signup(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')
			password = form.cleaned_data.get('password')
			User.objects.create_user(username=username,email=email, password=password)
			return redirect('login')
	else:
		form = SignupForm()

	context = {

		'form': form, 

	}

	return render(request, 'authy/signup.html', context)

def passwordchange(request):
	user = request.user
	if request.method == 'POST':
		form = ChangePasswordForm(request.POST)
		if form.is_valid():
			new_password = form.cleaned_data.get('new_password')
			user.set_password(new_password)
			user.save()
			update_session_auth_hash(request, user)
			return redirect('change_password_done')
	else:
		form = ChangePasswordForm(instance=user)

	context = {

		'form': form
	}

	return render(request, 'authy/change_password.html, context')



def passwordChangeDone(request):
	return render(request, 'change_password_done.html')



@login_required
def editProfile(request):
	user = request.user
	profile = Profile.objects.get(user=user)
	Base_Width = 400

	if request.method == 'POST':
		form = EditProfileForm(request.POST, request.FILES)
		if form.is_valid():
			profile.picture = form.cleaned_data.get('picture')
			profile.first_name = form.cleaned_data.get('first_name')
			profile.last_name = form.cleaned_data.get('last_name')
			profile.location = form.cleaned_data.get('location')
			profile.url = form.cleaned_data.get('url')
			profile.profile_info = form.cleaned_data.get('profile_info')
			profile.save()
			return redirect('index')
	else:
		form = EditProfileForm(instance=profile)

	context = {

		'form':form

	}

	return render(request, 'authy/edit_profile.html', context)



@login_required
def follow(request, username, option):

	following = get_object_or_404(User, username=username)

	try:

		f, created = Follow.objects.get_or_create(follower=request.user, following=following)

		if int(option) == 0:
			f.delete()
			Stream.objects.filter(following=following, user=request.user).all().delete()

		else:

			posts = Post.objects.all().filter(user=following)[:25]

			with transaction.atomic():
				for post in posts:
					stream = Stream(post=post, user=request.user, date=post.posted, following=following)
					stream.save()

		return HttpResponseRedirect(reverse('profile', args=[username]))
	except User.DoesNotExist:
		return HttpResponseRedirect(reverse('profile', args=[username]))










