from django.urls import path
from . import views 

urlpatterns = [
    path('' , views.signuppage , name='signup'),
    path('login/' , views.loginpage , name='login'),
    path('logout/' , views.logoutUser , name='logout'),
]

