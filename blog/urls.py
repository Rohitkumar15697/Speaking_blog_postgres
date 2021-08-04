
from django.urls import path,include
from .import views
from homeapp.views import search_result 


urlpatterns = [

    path('profile/',views.profile,name='profile'),
    path('addblog/', views.add_blog, name='addblog'),
    path('confirm_logout/',views.confirm_logout, name='confirmlogout'),
    path('logout/',views.logoutme,name='logout'),
    path('search/',search_result),
    path('delete_account/<int:pk>',views.DeleteAccount.as_view(), name='deleteaccount'),
    #add profile detail
    path('add_detail', views.add_profile_detail,name='adddetail'),
    #show user data
    path('profiledetail/<str:username>', views.Show_User_Data, name='profiledetail'),

]