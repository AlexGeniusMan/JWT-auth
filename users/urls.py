from django.conf.urls import url
from .views import CreateUserAPIView

urlpatterns = [
    url(r'^user/create/$', CreateUserAPIView.as_view()),
]