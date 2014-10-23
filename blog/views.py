from django.shortcuts import render, get_object_or_404
from blog.models import Post, Tag


def blog(request):
    return render(request, 'blog.html', {
        'posts': Post.objects.order_by('-created')
    })


def post(request, pk):
    post_obj = get_object_or_404(Post, pk=pk)

    return render(request, 'post.html', {
        'post': post_obj
    })


def posts_by_tag(request, tag_pk):
    tag = get_object_or_404(Tag, pk=tag_pk)

    return render(request, 'blog.html', {
        'tag': tag,
        'posts': tag.posts.order_by('-created')
    })


def error(request):
    my_variable = '!'
    my_list = ['testing', 'a', 'list', 'out']
    my_list = ["{}{}".format(list_item, my_variable) for list_item in my_list]
    raise NotImplementedError("Woops! This doesn't exist.")