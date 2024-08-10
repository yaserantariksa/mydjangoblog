from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Tag, Post, Page
from mysite.meta import site
# Create your views here.


def index(request):
    pages = Page.objects.all()
    search = ""
    if 'search' in request.GET:
        search = request.GET['search']


    data = Post.objects.filter(is_draft=False).filter(Q(tags__title__contains=search) | Q(title__contains=search)).order_by('-updated_at').distinct()


    paginator = Paginator(data, 10)
    page_number = request.GET.get("page")
    posts = paginator.get_page(page_number)
    tags = Tag.objects.all()

    context = {
        "site": site,
        "pages": pages,
        "title": 'HOME',
        'keywords' : ','.join(list(map(lambda t: t.title, tags))),
        "tags" : tags,
        "posts": posts,
        "search": search
    }
    return render(request, 'blog/index.html', context)

def post(request, slug):
    post = Post.objects.get(slug=slug)
    tags = Tag.objects.all()
    pages = Page.objects.all()

    context = {
        "site": site,
        "pages": pages,
        "title": post.title,
        'keywords' : ','.join(list(map(lambda t: t.title, tags))),
        'post_tags' : ','.join(list(map(lambda t: t.title, post.tags.all()))),
        "site": site,
        'post': post
    }

    return render(request, 'blog/post.html', context)
