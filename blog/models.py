
from django.db import models
# from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Post(models.Model):

    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # content = models.TextField()
    content = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/')
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    CATEGORY = {
        ('Frontend', 'Frontend'),
        ('Backend', 'Backend'),
        ('Fullstack', 'Fullstack'),
        ('Web3', 'Web3'),
        ('AWS-DevOps', 'AWS-DevOps'),
        ('Cyber Security', 'Cyber Security'),
        ('Salesforce', 'Salesforce'),
    }
    category = models.CharField(max_length=20, choices=CATEGORY)
    likes = models.ManyToManyField(User, related_name='blog_post')

    def total_likes(self):
        return self.likes.count()

    def total_comments(self):
        return self.comments.count()

    def __str__ (self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'id': self.id})


class UserProfile(models.Model):
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(null=True)
    website_url = models.CharField(max_length=300, null=True, blank=True)
    linkedin_url = models.CharField(max_length=300, null=True, blank=True)
    github_url = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.user.username  

    def get_absolute_url(self):
        return reverse('index')



class Comment(models.Model):
    
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField(null=True)
    message = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post.title + ' | ' + self.name