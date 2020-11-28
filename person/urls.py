from django.conf.urls import url
from person import views


urlpatterns=[
   url(r'details/',views.UserCreationAPI.as_view()),
   url(r'update/',views.UserUpdateAPI.as_view()),
]