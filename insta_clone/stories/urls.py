from django.urls import path


from .views import newStory, showMedia


urlpatterns = [
	path('newstory/', newStory, name='newstory'),
	path('showmedia/<stream_id>', showMedia, name='showmedia'),
]