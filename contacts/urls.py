from django.urls import path

from . import views

# This is like the routes to use for each app
urlpatterns = [
    path('contact', views.contact, name='contact'),
]
