from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings


from authy.views import userprofile, follow

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')), 
    path('authy/', include('authy.urls')),
    path('notifications/', include('notifications.urls')),
    path('directs/', include('directs.urls')),
    path('comments/', include('comment.urls')),
    path('stories/', include('stories.urls')),


    path('<username>/', userprofile, name='profile'),
    path('<username>/follow/<option>', follow, name='follow'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)