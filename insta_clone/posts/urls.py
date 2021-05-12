from django.urls import path
from .views import index, newpost, post_detail, like, favorite, tags

urlpatterns = [

	path('', index, name='index'),
	path('newpost/', newpost, name='newpost',), 
	path('<uuid:post_id>/', post_detail, name='postdetails'),
	path('<uuid:post_id>/like', like, name='postlikes'),
	path('<uuid:post_id>/favorite', favorite, name='postfavorites'), 
	path('tag/<slug:tag_slug>', tags, name='tags'),
]