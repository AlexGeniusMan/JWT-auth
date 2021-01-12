from django.conf.urls import url
import users.views as users_views

urlpatterns = [
    url(r'^user/create/$', users_views.CreateUserAPIView.as_view()),
    url(r'^user/obtain_token/$', users_views.AuthenticateUserView.as_view()),
    url(r'^user/update/$', users_views.UserRetrieveUpdateAPIView.as_view()),
]
