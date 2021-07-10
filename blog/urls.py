
from django.urls import path,include
from .import views
from homeapp.views import search_result 

urlpatterns = [

    path('profile/',views.profile,name='profile'),
    path('addblog/', views.add_blog, name='addblog'),
    path('logout/',views.logoutme,name='logout'),
    path('search/',search_result),

]