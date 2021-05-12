from django.urls import path

from .views import inbox, directs, userSearch, newConversation, sendDirect, ajax_view


urlpatterns = [

	path('', inbox, name='inbox'),
	path('directs/<username>', directs, name='directs'),
	path('new/', userSearch, name='usersearch'),
	path('new/<username>',newConversation, name='newconversation'),
	path('send/', sendDirect, name='send_direct'),
	path('loadmore/', ajax_view, name='ajax_view')

]