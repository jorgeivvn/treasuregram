from django.urls import include, path
from .views import index
from .views import show
from .views import post_treasure
from .views import profile
from .views import login_view
from .views import logout_view

urlpatterns = [
    path(r'', index),
    path('<treasure_id>', show, name = 'show'),
    path('post_url/', post_treasure, name= "post_treasure"),
    path('user/', profile, name = 'profile'),
    path('login/', login_view, name="login_view"),
    path('logout/', logout_view, name="logout_view")
]
