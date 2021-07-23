from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from django.db.models.signals import pre_save
from django.utils.text import slugify
# Create your models here.

class blogpost(models.Model):
   
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)
    topic=models.CharField(max_length=122,null=False)
    title=models.CharField(max_length=250,blank=False)
    slug=models.SlugField(null=True)
    post=models.TextField()
    #more other headings and their text which can only be added from admin pannel
    heading1=models.CharField(max_length=250,blank=True)
    post1=models.TextField(blank=True)
    heading2=models.CharField(max_length=250,blank=True)
    post2=models.TextField(blank=True)
    heading3=models.CharField(max_length=250,blank=True)
    post3=models.TextField(blank=True)

    likes=models.ManyToManyField(User, related_name='blog_posts',blank=True)
    date=models.DateTimeField(auto_now_add=True )

    class Meta:
        ordering=['-date']
    
    def __str__(self):
        return ' (' +str(self.created_by)+') Title- '+self.title
    
    def get_absolute_url(self):
        return reverse('homeapp:article', kwargs={'slug':self.slug})
    
def create_slug(instance, new_slug=None):
    slug=slugify(instance.title)
    if new_slug is not None:
        slug=new_slug
    qs=blogpost.objects.filter(slug=slug).order_by('-id')
    exists=qs.exists()
    if exists:
        new_slug="%s-%s" %(slug,qs.first().id)
        return create_slug(instance,new_slug=new_slug)
    return slug


def pre_save_blog_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug= create_slug(instance)

pre_save.connect(pre_save_blog_reciever,sender=blogpost)   
    


class CommentModel(models.Model):
    post = models.ForeignKey(blogpost ,related_name='comments', on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    comment_likes=models.ManyToManyField(User, related_name='comment_post')
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering=['-date_added']
    
    def __str__(self):
        return '%s - %s' %(self.post.title, self.name)

    





#User Profile detail
#class ProfileModel(models.Model):
