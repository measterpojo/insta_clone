from django.shortcuts import render, reverse
from .forms import CommentForm
from django.core import serializers

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse

from posts.models import Post

def comment_create_view(request, post_id , *args, **kwargs):
	posts = get_object_or_404(Post, id=post_id)

	if request.is_ajax and request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():

			instance = form.save(commit=False)
			instance.post = posts
			instance.user = request.user
			instance.save()

			ser_instance = serializers.serialize('json', [instance, ])

			return JsonResponse({'instance': ser_instance}, status=200)
		else:
			return JsonResponse({'error': form.errors}, status=400)

	return JsonResponse({'error': ''}, status=400)














	# posts = get_object_or_404(Post, id=post_id)
	# form = CommentForm(request.POST or None)

	# next_url = request.POST.get('next') or None
	# print(next_url)
	
	# if form.is_valid():
	# 	comment = form.save(commit=False)
	# 	comment.post = posts
	# 	comment.user = request.user
	# 	comment.save()
	# 	if next_url != None:
	# 		return redirect(next_url)
	# 	form = CommentForm()
	# 	return HttpResponseRedirect(reverse('postdetails', args=[post_id]))

	# context = {

	# 	'form': form 
	# }

	# return render(request, 'comments/comment.html', context)