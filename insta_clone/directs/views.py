from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from .models import Message
from django.contrib.auth.models import User

from django.db.models import Q
from django.core.paginator import Paginator

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, JsonResponse

@login_required
def inbox(request):
	messages = Message.get_messages(user=request.user)
	active_direct = None
	directs = None

	if messages:
		message = messages[0]
		active_direct = message['user'].username
		directs = Message.objects.filter(user=request.user, recipient=message['user'])
		directs.update(is_read=True)
		for message in messages:
			if message['user'].username == active_direct:
				message['unread'] = 0 

	context = {
		'directs': directs,
		'messages': messages,
		'active_direct':active_direct
		}

	return render(request, 'directs/direct.html', context)

@login_required
def userSearch(request):
	query = request.GET.get('q')
	next_url = request.GET.get('name') or None
	context = {}

	if next_url != None:
			return redirect(next_url)

	if query:
		users = User.objects.filter(Q(username__icontains=query))


		#pagaination
		paginator = Paginator(users, 6)
		page_number = request.GET.get('page')
		users_paginator = paginator.get_page(page_number)

		context = {
			'users': users_paginator

		}

	return render(request, 'directs/search_user.html', context)

@login_required
def directs(request, username):
	user = request.user
	messages = Message.get_messages(user=user)
	active_direct = username
	directs = Message.objects.filter(user=user, recipient__username=username)
	directs.update(is_read=True)
	for message in messages:
		if message['user'].username == username:
			message['unread'] = 0

	context = {
		'messages':messages,
		'directs':directs,
		'active_direct':active_direct,
	}

	return render(request, 'directs/direct.html', context)


@login_required
def newConversation(request, username):
	from_user = request.user
	body = ' Started a new conversation '
	try:
		to_user = User.objects.get(username=username)
	except Exception as e:
		return redirect('userSearch')
	if from_user != to_user:
		Message.send_message(from_user, to_user, body)
	return redirect('inbox')

@login_required
def sendDirect(request):
	from_user = request.user
	to_user_username = request.POST.get('to_user')
	body = request.POST.get('body')

	if request.method == 'POST':
		to_user = User.objects.get(username=to_user_username)
		Message.send_message(from_user, to_user, body)
		return redirect('inbox')
	else:
		HttpResponseBadRequest()

def checkDirects(request):
	directs_count = 0
	if request.user.is_authenticated:
		directs_count = Message.objects.filter(user=request.user, is_read=False).count()

	return {'directs_count': directs_count}




def ajax_view(request):
	pass
# 	user = request.user

# 	if request.is_ajax():
# 		username = request.POST.get('username')

# 		directs = Message.objects.filter(user=user, recipient__username=username).order_by('date').values(

# 			'body',
# 			'date',

# 			)


# 		directs_list = list(directs)

# 		for x in range(len(directs_list)):
# 			directs_list[x]['date'] = naturaltime(directs_list[x]['date'])

# 		return JsonResponse(directs_list, safe=False)

# 	else:

# 		return JsonResponse({'empty': True}, safe=False)




