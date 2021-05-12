from django.db import models
from django.contrib.auth.models import User

NOTIFICATION_TYPES = ((1,'Like'),(2,'Comment'), (3,'Follow'))


class Notification(models.Model):

	post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, related_name='noti_post', blank=True, null=True)
	sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='noti_from_user')
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='noti_to_user')
	notification_type = models.IntegerField(choices=NOTIFICATION_TYPES)
	text_preview = models.CharField(max_length=50, null=True, blank=True)
	date = models.DateTimeField(auto_now_add=True)
	is_seen = models.BooleanField(default=False)
