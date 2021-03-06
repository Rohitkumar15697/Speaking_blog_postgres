
from django.urls import path,include
from .import views
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from blog.models import blogpost

app_name='homeapp'



urlpatterns = [
    
    path('',views.index,name='home'),
    path('about', views.about, name='about'),
    path('privacy-policy', views.privacy_policy,name='privacypolicy'),
    path('search/',views.search_result,name='search'),
    path('listdata/',views.ListData.as_view(),name='listdata'),
    path('article/<slug:slug>',views.DetailData.as_view(),name='article'),
    path('editdata/<slug:slug>', login_required(views.EditBlog.as_view(template_name='edit_blog.html')), name='editblog'),
    path('deleteblog/<slug:slug>/remove',views.DeleteBlog.as_view(),name='deleteblog'),
    path('user_blogs/', views.user_blogs.as_view(), name='user_blogs'),
    #path('category/', views.category_list.as_view(),name='category'),  #perfomr link operation on index.html
    path('like/<slug:slug>', views.like_post, name='like_post'),
    path('article/<slug:slug>/comment', views.comment_view, name='comment'),
    path('article/<slug:slug>/deletecomment/<int:pk>', views.delete_comment, name='deletecomment'),


]