
from django.urls import path,include
from .import views
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from blog.models import blogpost

app_name='homeapp'



urlpatterns = [
    
    path('',views.index,name='home'),
    path('about', views.about, name='about'),
    path('search/',views.search_result,name='search'),
    path('listdata/',views.ListData.as_view(),name='listdata'),
    path('detaildata/<slug:slug>',views.DetailData.as_view(),name='detaildata'),
    path('editdata/<slug:slug>', login_required(views.EditBlog.as_view(template_name='edit_blog.html')), name='editblog'),
    path('deleteblog/<slug:slug>/remove',views.DeleteBlog.as_view(),name='deleteblog'),
    path('user_blogs/', views.user_blogs.as_view(), name='user_blogs'),
    #path('category/', views.category_list.as_view(),name='category'),  #perfomr link operation on index.html
    path('like/<slug:slug>', views.like_post, name='like_post'),
    path('detaildata/<slug:slug>/comment', views.comment_view, name='comment'),

]