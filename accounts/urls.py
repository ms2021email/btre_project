from django.urls import path

from . import views

# This is like the routes to use for each app
# Need a matching method
# Note there are multiple apps per project
urlpatterns = [
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('dashboard', views.dashboard, name='dashboard'),
]
