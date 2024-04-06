from django.urls import path
from user import views


urlpatterns = [

    path('login/', views.user_login, name='user_login'),
    path('signup/', views.signup, name="user_signup")

]
