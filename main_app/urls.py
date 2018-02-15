from django.urls import include, path
from .views import index
from .views import show
from .views import post_treasure

urlpatterns = [
    path(r'', index),
    path('<treasure_id>', show, name = 'show'),
    path('post_url/', post_treasure, name= "post_treasure")
]
