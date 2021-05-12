from django.urls import path

from django.contrib.auth import views as authViews

from .views import signup, editProfile, login_request

urlpatterns = [


	path('login/', login_request, name='login'),
	path('logout/', authViews.LogoutView.as_view(), name='logout'),
	path('signup/', signup , name='signup'),
	path('editproflie', editProfile, name='edit-profile')
]