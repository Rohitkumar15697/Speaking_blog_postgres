from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class blogpost(models.Model):
   
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)
    topic=models.CharField(max_length=122,null=False)
    title=models.CharField(max_length=250,blank=False)
    post=models.TextField()
    likes=models.ManyToManyField(User, related_name='blog_posts')
    date=models.DateTimeField(auto_now_add=True )


    def __str__(self):
        return ' (' +str(self.created_by)+') Title- '+self.title
    
    class Meta:
        ordering=['-date']
    
    def get_absolute_url(self):
        return reverse("home:detaildata",args=[str(self.id)])
    


class CommentModel(models.Model):
    post = models.ForeignKey(blogpost ,related_name='comments', on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    comment_likes=models.ManyToManyField(User, related_name='comment_post')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' %(self.post.title, self.name)

    class Meta:
        ordering=['-date_added']

    def get_absolute_url(self):
        return reverse("home:comment",args=[str(self.id)])


#User Profile detail
#class ProfileModel(models.Model):
