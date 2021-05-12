from django.urls import path

from .views import showNotifactions, deleteNotification


urlpatterns =[

	path('', showNotifactions, name='show-notifications'),
	path('<noti_id>/delete', deleteNotification, name='delete-notification')
]