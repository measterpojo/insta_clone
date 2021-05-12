from django.urls import path
from .views import comment_create_view

urlpatterns = [
	path('comment/<uuid:post_id>/', comment_create_view, name='new_comments'),
]