from blog.models import Post, Tag


def latest_post(request):
    return {
        'latest_post': Post.objects.latest('created')
    }


def tags(request):
    return {
        'tags': Tag.objects.all()
    }