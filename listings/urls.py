from django.urls import path

from . import views

# This is like the routes to use for each app
# Need a matching method
# Note there are multiple apps per project
urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
]
