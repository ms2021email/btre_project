from django.urls import path

from . import views

# This is like the routes to use for each app
# Need a matching method
# Note there are multiple apps per project
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
]
