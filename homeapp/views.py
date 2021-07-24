from typing import List
from blog.forms import Myblogform
from django.shortcuts import redirect, render,render,HttpResponse,get_object_or_404
from django.http import HttpResponseRedirect
from blog.models import blogpost,CommentModel
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView,DeleteView,UpdateView
from django.urls import reverse_lazy,reverse

#for counting the number of likes 
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q

# Create your views here.

def index(request):
    count=len(blogpost.objects.all())
    postdata=list(blogpost.objects.all()[:15])
    
    #This is for showing topic names in index page
    topic_names=blogpost.objects.values_list('topic',flat=True).distinct() 

    blog_data=postdata[:3]
    context={'data':postdata,'blog_data':blog_data,'topics':topic_names,'count':count}
    
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')




def search_result(request):
    search_element=request.GET.get('search_me').strip()
    if search_element=="":
        return HttpResponse('No data for search!')
    else:
        search_data=blogpost.objects.all().filter(Q(title__icontains=search_element) | Q(topic__istartswith=search_element))
        count=len(search_data)
        print(search_result)
    
        return render(request,'search_result.html',{'searched':search_element,'result':search_data,'count':count})



#Listing the blogs when we click on all blogs from index page

class ListData(ListView):
    model=blogpost
    context_object_name='data'
    template_name='blogpost_list.html'






#detail of every blog when we click on any blog title

class DetailData(DetailView):
    model=blogpost
    template_name='blogpost_detail.html'
    context_object_name='data'

    def get_context_data(self, **kwargs):
        context= super(DetailData,self).get_context_data(**kwargs)
        context['list_titles']=blogpost.objects.annotate(likes_count=Count('likes')).order_by('-likes_count')[:6]
        return context




'''
#This code is for update blog post
@method_decorator(login_required, name='dispatch')
class UpdateBlog(UpdateView):
    model=blogpost
    template_name='edit_blog.html'
    '''
   

@method_decorator(login_required, name='dispatch')
class EditBlog(UpdateView):
    model=blogpost
    form_class=Myblogform
    template_name='edit_blog.html'
    success_url=reverse_lazy('profile')



#Delete the blog post with this view class

class DeleteBlog(DeleteView):
    model=blogpost
    template_name='delete_blog.html'
    success_url=reverse_lazy('profile') #This shows- When delete is successfull then where to go!


class user_blogs(ListView):
    model=blogpost
    template_name='blogpost_list.html'
    def get_queryset(self):
        return blogpost.objects.all().filter(created_by=self.request.user)
    
'''
class category_list(ListView):
    model=blogpost
    template_name='blogpost_list.html'
    def get_queryset(self):
        return blogpost.objects.all().filter(topic=self.request.GET.get('cate'))'''

@login_required(login_url='index')
def like_post(request, slug):
    post=get_object_or_404(blogpost, slug=request.POST.get('like'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        
    else:
        post.likes.add(request.user)
        
    
    return redirect('homeapp:article',slug)


def comment_view(request, slug):
    if request.method=='POST' and 'comment_button' in request.POST:
        
        body=request.POST.get('comment_text')

        post=get_object_or_404(blogpost, slug=slug)
        name=get_object_or_404(User, pk=request.user.id)
        obj=CommentModel(body=body)
        obj.name=name
        obj.post=post
        obj.save()
        return HttpResponseRedirect(reverse('homeapp:article',args=[slug]))
    



    
