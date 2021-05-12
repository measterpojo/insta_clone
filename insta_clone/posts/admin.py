from django.contrib import admin

from .models import Post, Follow, Stream, Likes, Tag


admin.site.register(Follow)
admin.site.register(Post)
admin.site.register(Stream)
admin.site.register(Likes)
admin.site.register(Tag)
