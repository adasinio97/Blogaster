from django.shortcuts import render, get_object_or_404
from .models import Post, BlogClass, Comment
from .forms import PostForm, BlogForm, CommentForm
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from account.models import Profile


def blogi(request):
    blogs = BlogClass.objects.order_by('-created_date')
    profile = Profile.objects.all()
    return render(request, 'Blog/Blogi.html', {'blogs': blogs, 'profile': profile})


def add_comment_to_post(request, pk, id_blogu):
    post = get_object_or_404(Post, pk=pk)
    pk = pk
    blog = get_object_or_404(BlogClass, pk=id_blogu)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk, id_blogu=id_blogu)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form, 'pk': pk, 'blog': blog})


def post_list(request, pk):
    pk = pk
    blog_id = get_object_or_404(BlogClass, pk=pk)
    posts = Post.objects.order_by('-created_date')
    profile = Profile.objects.all()
    return render(request, 'Blog/post_list.html', {'posts': posts, "profile": profile, 'blog_id': blog_id, "pk":pk})

@login_required
def post_detail(request, pk, id_blogu):
    pk = pk
    blog = get_object_or_404(BlogClass,pk=id_blogu)
    post = get_object_or_404(Post, pk=pk)
    profile = Profile.objects.all()
    comments = Comment.objects.filter(post=post).order_by('-created_date')
    return render(request, 'blog/post_detail.html', {'post': post, "profile": profile, "pk": pk, "blog": blog,
                                                     'comments': comments, 'id': id_blogu})


@login_required
def post_author(request, pk, id_blogu):
    blog = get_object_or_404(BlogClass, pk=id_blogu)
    author = Profile.objects.get(pk=pk)
    profile = Profile.objects.all()
    return render(request, 'blog/post_author.html', {'blog': blog, 'author': author, 'profile': profile})


@login_required
def blog_new(request):
    profile = Profile.objects.all()
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.published_date = timezone.now()
            blog.save()
            messages.success(request, 'Pomyślie stworzyłeś nowy blog!')
            return redirect('/')
    else:
        form = BlogForm()
    return render(request, 'blog/blog_edit.html', {'form': form, "profile": profile})
@login_required
def post_new(request, pk):
    pk = pk
    blog = get_object_or_404(BlogClass, pk=pk)
    profile = Profile.objects.all()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.blog = blog
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk, id_blogu = pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form,  "profile": profile, "pk": pk, "blog": blog})


@login_required
def post_edit(request, pk, id_blogu):
    pk = pk
    blog = get_object_or_404(BlogClass, pk=id_blogu)
    profile = Profile.objects.all()
    post = get_object_or_404(Post, pk=pk)
    if request.user==post.author    :
        if request.method == "POST":
            form = PostForm(request.POST, instance=post,files=request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.author =request.user
                post.published_date = timezone.now()
                post.save()
                messages.success(request, 'Edycja posta przebiegła pomyślnie!')
                return redirect('post_detail', pk=post.pk, id_blogu=id_blogu)
        else:
            form = PostForm(instance=post)
    else:
        messages.error(request, 'Nie możesz edytować tego post! Nie jesteś jego autorem!')
        return redirect('/', pk=post.pk)
    return render(request, 'blog/post_edit.html', {'form': form,  "profile": profile, "pk": pk, "blog": blog})


def add_comment_to_comment(request, com_id, pk, id_blogu):
    post = get_object_or_404(Post, pk=pk)
    pk = pk
    blog = get_object_or_404(BlogClass, pk=id_blogu)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.com = Comment.objects.get(id=com_id)
            comment.save()
            return redirect('post_detail', pk=post.pk, id_blogu=id_blogu)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form, 'pk': pk, 'blog': blog})