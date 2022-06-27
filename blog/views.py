from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import CommentForm, CreatePost, UserForm
from blog.models import Post, Comment
from django.urls import reverse_lazy, reverse
from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect

# def _get_form(request, formcls, prefix):
#     data = request.POST if prefix in request.POST else None
#     return formcls(data, prefix=prefix)
    

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('detail', args=[int(pk)]))
    


def HomeView(request):
    posts = Post.objects.all().order_by('-last_updated')

    registerform = UserForm()
    loginform = AuthenticationForm(request, data=request.POST)

    if loginform.is_valid():
        user = loginform.get_user()
        login(request, user)
        return redirect('index')


    if request.method == "POST" and 'registerform' in request.POST:
        registerform = UserForm(request.POST)

        if registerform.is_valid():
            user = registerform.save()
            login(request, user)
            return redirect('index')
        
    context = {
        'posts' : posts,
        'loginform' : loginform,
        'registerform' : registerform,
    }

    return render(request, 'blog/index.html', context)
 



def ArticleDetailView(request, id):
    post = get_object_or_404(Post, id=id)
    comments = post.comments.all()

    registerform = UserForm()
    loginform = AuthenticationForm(request, data=request.POST)
    commentform = CommentForm()

    if loginform.is_valid():
        user = loginform.get_user()
        login(request, user)
        return redirect('index')


    if request.method == "POST" and 'registerform' in request.POST:
        registerform = UserForm(request.POST)

        if registerform.is_valid():
            user = registerform.save()
            login(request, user)
            return redirect('index')

    # if request.user.is_authenticated:
    #     Post.objects.get_or_create(user=request.user, post=post)
    if request.method == "POST" and 'commentform' in request.POST:
        name = request.POST.get("name")
        message = request.POST.get("message")
        email = request.POST.get('email')

        newComment = Comment(name  = name, message = message, email = email)
        newComment.post = post
        newComment.user = request.user
        newComment.save()
        return redirect("detail", id=id)

    context = {
        "post":post,
        "comments":comments, 
        'loginform' : loginform,
        'registerform' : registerform,
        'commentform' : commentform,
    }
    return render(request,"blog/detail.html", context)


# def addComment(request,slug):
#     article = get_object_or_404(Article, slug=slug)

#     if request.method == "POST":
#         comment_author = request.POST.get("comment_author")
#         comment_content = request.POST.get("comment_content")

#         newComment = Comment(comment_author  = comment_author, comment_content = comment_content)

#         newComment.article = article

#         newComment.save()
#     return redirect(reverse("article:detail",kwargs={"slug":slug}))
       


def AddPostView(request):
    form = CreatePost()
    if request.method == 'POST':
        form = CreatePost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('index')

    return render(request, 'blog/add_post.html', {'form' : form})


    
class UpdatePostView(UpdateView):
    model = Post
    template_name = 'blog/update_post.html'
    fields = ('title', 'content', 'image', 'category',)

class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('index')


def user_logout(request):
    
    logout(request)
    return redirect('index')

def ProfileView(request, id):
    pass



class AboutView(TemplateView):
    template_name = 'blog/about.html'